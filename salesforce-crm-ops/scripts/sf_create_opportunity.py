#!/usr/bin/env python3
"""
Create or update a Salesforce Opportunity.
Supports dry-run mode, config-based field mapping, and VC-specific custom fields.

Usage:
    # Dry run
    python3 sf_create_opportunity.py --dry-run --name "ExampleAI Seed" --stage "First Meeting" --close-date 2026-03-31

    # Create opportunity
    python3 sf_create_opportunity.py --name "ExampleAI Seed" --stage "First Meeting" --close-date 2026-03-31

    # With VC-specific fields
    python3 sf_create_opportunity.py --name "ExampleAI Seed" --stage "Diligence" --close-date 2026-03-31 \
        --amount 2000000 --next-step "Schedule customer calls" --thesis-tag "AI Security" \
        --pass-reason "" --what-would-change ""

    # Update existing opportunity
    python3 sf_create_opportunity.py --id 006XXXX --stage "Passed" --pass-reason "Market too small" \
        --what-would-change "If TAM evidence shows >$1B"
"""

import os
import sys
import json
import argparse
import datetime
from pathlib import Path

import requests
import yaml


def load_config(config_dir: str) -> dict:
    """Load field mappings and stages from config files."""
    config = {"field_map": {}, "stages": {}, "required_fields": {}}
    config_path = Path(config_dir)
    
    if (config_path / "field_map.yaml").exists():
        with open(config_path / "field_map.yaml") as f:
            config["field_map"] = yaml.safe_load(f) or {}
    
    if (config_path / "stages.yaml").exists():
        with open(config_path / "stages.yaml") as f:
            config["stages"] = yaml.safe_load(f) or {}
    
    if (config_path / "required_fields.yaml").exists():
        with open(config_path / "required_fields.yaml") as f:
            config["required_fields"] = yaml.safe_load(f) or {}
    
    return config


def get_field_name(config: dict, obj: str, logical_name: str) -> str:
    """Map logical field name to Salesforce API field name."""
    if obj in config.get("field_map", {}) and logical_name in config["field_map"][obj]:
        return config["field_map"][obj][logical_name]
    defaults = {
        "name": "Name",
        "stage": "StageName",
        "close_date": "CloseDate",
        "amount": "Amount",
        "account_id": "AccountId",
        "next_step": "NextStep",
        "probability": "Probability",
        "description": "Description",
    }
    return defaults.get(logical_name, logical_name)


def get_stage_value(config: dict, logical_stage: str) -> str:
    """Map logical stage to Salesforce picklist value."""
    stages = config.get("stages", {}).get("opportunity_stages", {})
    return stages.get(logical_stage, logical_stage)


def env(name: str, default: str = None, required: bool = True) -> str:
    v = os.getenv(name, default)
    if required and not v:
        print(f"Missing {name}", file=sys.stderr)
        sys.exit(2)
    return v


def api_version() -> str:
    return os.getenv("SF_API_VERSION", "v59.0")


def base_url() -> str:
    return env("SF_BASE_URL").rstrip("/")


def token() -> str:
    return env("SF_ACCESS_TOKEN")


def create_opportunity(fields: dict) -> dict:
    url = f"{base_url()}/services/data/{api_version()}/sobjects/Opportunity/"
    r = requests.post(
        url,
        headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"},
        data=json.dumps(fields),
        timeout=30
    )
    if r.status_code >= 400:
        raise RuntimeError(f"Create Opportunity failed ({r.status_code}): {r.text}")
    return r.json()


def update_opportunity(opp_id: str, fields: dict) -> None:
    url = f"{base_url()}/services/data/{api_version()}/sobjects/Opportunity/{opp_id}"
    r = requests.patch(
        url,
        headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"},
        data=json.dumps(fields),
        timeout=30
    )
    if r.status_code >= 400:
        raise RuntimeError(f"Update Opportunity failed ({r.status_code}): {r.text}")


def validate_required_fields(config: dict, fields: dict, is_update: bool) -> list:
    """Check if required fields are present (only for create)."""
    if is_update:
        return []
    required = config.get("required_fields", {}).get("opportunity", ["Name", "StageName", "CloseDate"])
    missing = [f for f in required if f not in fields or not fields[f]]
    return missing


def main() -> None:
    p = argparse.ArgumentParser(description="Create or update a Salesforce Opportunity.")
    
    # Identifier for update
    p.add_argument("--id", help="Opportunity ID (for update)")
    
    # Core fields
    p.add_argument("--name", help="Opportunity name (required for create)")
    p.add_argument("--stage", help="Stage name (maps through config/stages.yaml)")
    p.add_argument("--close-date", help="Close date YYYY-MM-DD (required for create)")
    p.add_argument("--account-id", help="Related Account ID")
    p.add_argument("--amount", type=float, help="Deal amount")
    p.add_argument("--probability", type=int, help="Probability percentage")
    p.add_argument("--next-step", help="Next step description")
    p.add_argument("--description", help="Description/notes")
    
    # VC-specific custom fields
    p.add_argument("--thesis-tag", help="Thesis tag (custom field)")
    p.add_argument("--pass-reason", help="Pass reason (custom field)")
    p.add_argument("--what-would-change", help="What would change our mind (custom field)")
    p.add_argument("--recheck-date", help="Recheck date YYYY-MM-DD (custom field)")
    
    # Config and modes
    p.add_argument("--config", default="./config", help="Path to config directory")
    p.add_argument("--dry-run", action="store_true", help="Validate without executing")
    p.add_argument("--verbose", action="store_true", help="Show detailed output")
    
    args = p.parse_args()
    
    is_update = bool(args.id)
    
    # Validate required args for create
    if not is_update:
        if not args.name:
            print("Error: --name is required for create", file=sys.stderr)
            sys.exit(2)
        if not args.stage:
            print("Error: --stage is required for create", file=sys.stderr)
            sys.exit(2)
        if not args.close_date:
            print("Error: --close-date is required for create", file=sys.stderr)
            sys.exit(2)
    
    # Validate date format
    if args.close_date:
        try:
            datetime.date.fromisoformat(args.close_date)
        except ValueError:
            print("Error: --close-date must be YYYY-MM-DD format", file=sys.stderr)
            sys.exit(2)
    
    if args.recheck_date:
        try:
            datetime.date.fromisoformat(args.recheck_date)
        except ValueError:
            print("Error: --recheck-date must be YYYY-MM-DD format", file=sys.stderr)
            sys.exit(2)
    
    # Load config
    config = load_config(args.config)
    
    # Build fields dict
    fields = {}
    
    if args.name:
        fields[get_field_name(config, "opportunity", "name")] = args.name
    if args.stage:
        stage_value = get_stage_value(config, args.stage)
        fields[get_field_name(config, "opportunity", "stage")] = stage_value
    if args.close_date:
        fields[get_field_name(config, "opportunity", "close_date")] = args.close_date
    if args.account_id:
        fields[get_field_name(config, "opportunity", "account_id")] = args.account_id
    if args.amount is not None:
        fields[get_field_name(config, "opportunity", "amount")] = args.amount
    if args.probability is not None:
        fields[get_field_name(config, "opportunity", "probability")] = args.probability
    if args.next_step:
        fields[get_field_name(config, "opportunity", "next_step")] = args.next_step
    if args.description:
        fields[get_field_name(config, "opportunity", "description")] = args.description
    
    # Custom fields
    if args.thesis_tag:
        fields[get_field_name(config, "opportunity", "thesis_tag")] = args.thesis_tag
    if args.pass_reason is not None:  # Allow empty string to clear
        fields[get_field_name(config, "opportunity", "pass_reason")] = args.pass_reason
    if args.what_would_change is not None:
        fields[get_field_name(config, "opportunity", "what_would_change")] = args.what_would_change
    if args.recheck_date:
        fields[get_field_name(config, "opportunity", "recheck_date")] = args.recheck_date
    
    # Validate required fields
    missing = validate_required_fields(config, fields, is_update)
    if missing:
        print(f"Error: Missing required fields: {missing}", file=sys.stderr)
        sys.exit(2)
    
    # Dry run mode
    if args.dry_run:
        print("=== DRY RUN MODE ===")
        if is_update:
            print(f"Would UPDATE Opportunity {args.id} with fields:")
        else:
            print("Would CREATE Opportunity with fields:")
        print(json.dumps(fields, indent=2))
        print("\nValidation: PASSED")
        return
    
    # Execute
    if is_update:
        update_opportunity(args.id, fields)
        print(json.dumps({"action": "updated", "id": args.id}, indent=2))
    else:
        result = create_opportunity(fields)
        print(json.dumps({"action": "created", "id": result.get("id")}, indent=2))


if __name__ == "__main__":
    main()
