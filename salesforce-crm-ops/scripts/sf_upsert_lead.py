#!/usr/bin/env python3
"""
Upsert a Salesforce Lead by email or external ID.
Supports dry-run mode, config-based field mapping, and custom fields.

Usage:
    # Dry run (validate without creating)
    python3 sf_upsert_lead.py --dry-run --email founder@company.com --first Ada --last Lovelace --company ExampleAI

    # Create/update lead
    python3 sf_upsert_lead.py --email founder@company.com --first Ada --last Lovelace --company ExampleAI

    # Upsert by external ID
    python3 sf_upsert_lead.py --external-id External_ID__c --external-id-value "abc123" --first Ada --last Lovelace --company ExampleAI

    # With custom fields
    python3 sf_upsert_lead.py --email founder@company.com --first Ada --last Lovelace --company ExampleAI \
        --thesis-tag "AI Security" --signal-score 4 --must-be-true "Enterprise buyers will pay"
"""

import os
import sys
import json
import argparse
from pathlib import Path
from urllib.parse import quote_plus

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
    # Default mappings if no config
    defaults = {
        "email": "Email",
        "first_name": "FirstName",
        "last_name": "LastName",
        "company": "Company",
        "title": "Title",
        "website": "Website",
        "status": "Status",
        "source": "LeadSource",
        "description": "Description",
    }
    return defaults.get(logical_name, logical_name)


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


def soql_query(soql: str) -> dict:
    q = quote_plus(soql)
    url = f"{base_url()}/services/data/{api_version()}/query/?q={q}"
    r = requests.get(url, headers={"Authorization": f"Bearer {token()}"}, timeout=30)
    if r.status_code >= 400:
        raise RuntimeError(f"SOQL query failed ({r.status_code}): {r.text}")
    return r.json()


def create_lead(fields: dict) -> str:
    url = f"{base_url()}/services/data/{api_version()}/sobjects/Lead/"
    r = requests.post(
        url,
        headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"},
        data=json.dumps(fields),
        timeout=30
    )
    if r.status_code >= 400:
        raise RuntimeError(f"Create Lead failed ({r.status_code}): {r.text}")
    return r.json().get("id")


def update_lead(lead_id: str, fields: dict) -> None:
    url = f"{base_url()}/services/data/{api_version()}/sobjects/Lead/{lead_id}"
    r = requests.patch(
        url,
        headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"},
        data=json.dumps(fields),
        timeout=30
    )
    if r.status_code >= 400:
        raise RuntimeError(f"Update Lead failed ({r.status_code}): {r.text}")


def upsert_by_external_id(external_id_field: str, external_id_value: str, fields: dict) -> dict:
    """Upsert using Salesforce's native external ID upsert."""
    url = f"{base_url()}/services/data/{api_version()}/sobjects/Lead/{external_id_field}/{external_id_value}"
    r = requests.patch(
        url,
        headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"},
        data=json.dumps(fields),
        timeout=30
    )
    if r.status_code >= 400:
        raise RuntimeError(f"Upsert Lead failed ({r.status_code}): {r.text}")
    
    # 201 = created, 204 = updated
    if r.status_code == 201:
        return {"action": "created", "id": r.json().get("id")}
    else:
        return {"action": "updated", "id": external_id_value}


def validate_required_fields(config: dict, fields: dict) -> list:
    """Check if required fields are present."""
    required = config.get("required_fields", {}).get("lead", ["LastName", "Company", "Status"])
    missing = [f for f in required if f not in fields or not fields[f]]
    return missing


def main() -> None:
    p = argparse.ArgumentParser(description="Upsert a Salesforce Lead with config support and dry-run mode.")
    
    # Core fields
    p.add_argument("--email", help="Lead email address")
    p.add_argument("--first", help="First name")
    p.add_argument("--last", required=True, help="Last name (required)")
    p.add_argument("--company", required=True, help="Company name (required)")
    p.add_argument("--title", help="Job title")
    p.add_argument("--website", help="Company website")
    p.add_argument("--status", default="Open - Not Contacted", help="Lead status")
    p.add_argument("--source", help="Lead source")
    p.add_argument("--description", help="Description/notes")
    
    # Custom fields for VC workflows
    p.add_argument("--thesis-tag", help="Thesis tag (custom field)")
    p.add_argument("--signal-score", type=int, help="Signal score 1-5 (custom field)")
    p.add_argument("--must-be-true", help="Must be true statement (custom field)")
    p.add_argument("--pass-reason", help="Pass reason (custom field)")
    p.add_argument("--recheck-date", help="Recheck date YYYY-MM-DD (custom field)")
    
    # External ID upsert
    p.add_argument("--external-id", help="External ID field name for upsert (e.g., External_ID__c)")
    p.add_argument("--external-id-value", help="External ID value for upsert")
    
    # Config and modes
    p.add_argument("--config", default="./config", help="Path to config directory")
    p.add_argument("--dry-run", action="store_true", help="Validate without executing")
    p.add_argument("--verbose", action="store_true", help="Show detailed output")
    
    args = p.parse_args()
    
    # Load config
    config = load_config(args.config)
    
    # Build fields dict using config mappings
    fields = {}
    
    if args.first:
        fields[get_field_name(config, "lead", "first_name")] = args.first
    fields[get_field_name(config, "lead", "last_name")] = args.last
    fields[get_field_name(config, "lead", "company")] = args.company
    fields[get_field_name(config, "lead", "status")] = args.status
    
    if args.email:
        fields[get_field_name(config, "lead", "email")] = args.email
    if args.title:
        fields[get_field_name(config, "lead", "title")] = args.title
    if args.website:
        fields[get_field_name(config, "lead", "website")] = args.website
    if args.source:
        fields[get_field_name(config, "lead", "source")] = args.source
    if args.description:
        fields[get_field_name(config, "lead", "description")] = args.description
    
    # Custom fields
    if args.thesis_tag:
        fields[get_field_name(config, "lead", "thesis_tag")] = args.thesis_tag
    if args.signal_score is not None:
        fields[get_field_name(config, "lead", "signal_score")] = args.signal_score
    if args.must_be_true:
        fields[get_field_name(config, "lead", "must_be_true")] = args.must_be_true
    if args.pass_reason:
        fields[get_field_name(config, "lead", "pass_reason")] = args.pass_reason
    if args.recheck_date:
        fields[get_field_name(config, "lead", "recheck_date")] = args.recheck_date
    
    # Validate required fields
    missing = validate_required_fields(config, fields)
    if missing:
        print(f"Error: Missing required fields: {missing}", file=sys.stderr)
        sys.exit(2)
    
    # Dry run mode
    if args.dry_run:
        print("=== DRY RUN MODE ===")
        print(f"Would upsert Lead with fields:")
        print(json.dumps(fields, indent=2))
        if args.external_id:
            print(f"\nUsing external ID: {args.external_id} = {args.external_id_value}")
        elif args.email:
            print(f"\nWould query for existing Lead by email: {args.email}")
        print("\nValidation: PASSED")
        return
    
    # Execute upsert
    if args.external_id and args.external_id_value:
        # Use native Salesforce external ID upsert
        result = upsert_by_external_id(args.external_id, args.external_id_value, fields)
        print(json.dumps(result, indent=2))
    elif args.email:
        # Query by email and create/update
        email = args.email.replace("'", "\\'")
        result = soql_query(f"SELECT Id FROM Lead WHERE Email='{email}' LIMIT 1")
        records = result.get("records", [])
        
        if records:
            lead_id = records[0]["Id"]
            update_lead(lead_id, fields)
            print(json.dumps({"action": "updated", "id": lead_id}, indent=2))
        else:
            lead_id = create_lead(fields)
            print(json.dumps({"action": "created", "id": lead_id}, indent=2))
    else:
        # No identifier - create new
        lead_id = create_lead(fields)
        print(json.dumps({"action": "created", "id": lead_id}, indent=2))


if __name__ == "__main__":
    main()
