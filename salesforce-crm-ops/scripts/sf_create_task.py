#!/usr/bin/env python3
"""
Create a Salesforce Task for next-step tracking.
Supports dry-run mode, config-based field mapping, and VC-specific workflows.

Usage:
    # Dry run
    python3 sf_create_task.py --dry-run --subject "Follow up: send customer intro" --due 2026-02-05

    # Create task linked to opportunity
    python3 sf_create_task.py --subject "Schedule diligence calls" --due 2026-02-05 --what-id 006XXXX

    # Create task linked to lead
    python3 sf_create_task.py --subject "First meeting follow-up" --due 2026-02-03 --who-id 00QXXXX

    # High priority task
    python3 sf_create_task.py --subject "IC prep" --due 2026-02-10 --priority High --what-id 006XXXX
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
        "subject": "Subject",
        "due_date": "ActivityDate",
        "status": "Status",
        "priority": "Priority",
        "what_id": "WhatId",
        "who_id": "WhoId",
        "description": "Description",
    }
    return defaults.get(logical_name, logical_name)


def get_status_value(config: dict, logical_status: str) -> str:
    """Map logical status to Salesforce picklist value."""
    statuses = config.get("stages", {}).get("task_statuses", {})
    return statuses.get(logical_status, logical_status)


def get_priority_value(config: dict, logical_priority: str) -> str:
    """Map logical priority to Salesforce picklist value."""
    priorities = config.get("stages", {}).get("task_priorities", {})
    return priorities.get(logical_priority.lower(), logical_priority)


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


def create_task(fields: dict) -> dict:
    url = f"{base_url()}/services/data/{api_version()}/sobjects/Task/"
    r = requests.post(
        url,
        headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"},
        data=json.dumps(fields),
        timeout=30
    )
    if r.status_code >= 400:
        raise RuntimeError(f"Create Task failed ({r.status_code}): {r.text}")
    return r.json()


def validate_required_fields(config: dict, fields: dict) -> list:
    """Check if required fields are present."""
    required = config.get("required_fields", {}).get("task", ["Subject"])
    missing = [f for f in required if f not in fields or not fields[f]]
    return missing


def main() -> None:
    p = argparse.ArgumentParser(description="Create a Salesforce Task for next-step tracking.")
    
    # Core fields
    p.add_argument("--subject", required=True, help="Task subject (required)")
    p.add_argument("--due", required=True, help="Due date YYYY-MM-DD (required)")
    p.add_argument("--status", default="Not Started", help="Task status")
    p.add_argument("--priority", default="Normal", help="Task priority (High/Normal/Low)")
    p.add_argument("--what-id", help="Related record ID (Opportunity/Account)")
    p.add_argument("--who-id", help="Name record ID (Lead/Contact)")
    p.add_argument("--description", help="Task description/comments")
    
    # Config and modes
    p.add_argument("--config", default="./config", help="Path to config directory")
    p.add_argument("--dry-run", action="store_true", help="Validate without executing")
    p.add_argument("--verbose", action="store_true", help="Show detailed output")
    
    args = p.parse_args()
    
    # Validate date format
    try:
        datetime.date.fromisoformat(args.due)
    except ValueError:
        print("Error: --due must be YYYY-MM-DD format", file=sys.stderr)
        sys.exit(2)
    
    # Load config
    config = load_config(args.config)
    
    # Build fields dict
    fields = {
        get_field_name(config, "task", "subject"): args.subject,
        get_field_name(config, "task", "due_date"): args.due,
        get_field_name(config, "task", "status"): get_status_value(config, args.status),
        get_field_name(config, "task", "priority"): get_priority_value(config, args.priority),
    }
    
    if args.what_id:
        fields[get_field_name(config, "task", "what_id")] = args.what_id
    if args.who_id:
        fields[get_field_name(config, "task", "who_id")] = args.who_id
    if args.description:
        fields[get_field_name(config, "task", "description")] = args.description
    
    # Validate required fields
    missing = validate_required_fields(config, fields)
    if missing:
        print(f"Error: Missing required fields: {missing}", file=sys.stderr)
        sys.exit(2)
    
    # Dry run mode
    if args.dry_run:
        print("=== DRY RUN MODE ===")
        print("Would CREATE Task with fields:")
        print(json.dumps(fields, indent=2))
        print("\nValidation: PASSED")
        return
    
    # Execute
    result = create_task(fields)
    print(json.dumps({"action": "created", "id": result.get("id")}, indent=2))


if __name__ == "__main__":
    main()
