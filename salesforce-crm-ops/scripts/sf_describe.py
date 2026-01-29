#!/usr/bin/env python3
"""
Salesforce schema discovery script.
Describes objects to reveal fields, required fields, and picklist values.

Usage:
    python3 sf_describe.py Lead
    python3 sf_describe.py Lead Account Opportunity
    python3 sf_describe.py Lead --output schema.json
"""

import os
import sys
import json
import argparse
import requests

def get_env_or_exit(name: str) -> str:
    val = os.environ.get(name)
    if not val:
        print(f"Error: {name} environment variable not set", file=sys.stderr)
        sys.exit(1)
    return val

def get_access_token() -> str:
    """Get access token from env or request new one."""
    token = os.environ.get("SF_ACCESS_TOKEN")
    if token:
        return token
    
    base_url = get_env_or_exit("SF_BASE_URL")
    client_id = get_env_or_exit("SF_CLIENT_ID")
    client_secret = get_env_or_exit("SF_CLIENT_SECRET")
    
    token_url = f"{base_url}/services/oauth2/token"
    resp = requests.post(token_url, data={
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    })
    resp.raise_for_status()
    return resp.json()["access_token"]

def describe_object(base_url: str, token: str, object_name: str, api_version: str) -> dict:
    """Describe a Salesforce object."""
    url = f"{base_url}/services/data/{api_version}/sobjects/{object_name}/describe"
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()

def format_field_info(field: dict) -> dict:
    """Extract relevant field information."""
    info = {
        "name": field["name"],
        "label": field["label"],
        "type": field["type"],
        "required": not field["nillable"] and not field["defaultedOnCreate"],
        "createable": field["createable"],
        "updateable": field["updateable"],
    }
    
    if field["type"] == "picklist" and field.get("picklistValues"):
        info["picklist_values"] = [
            pv["value"] for pv in field["picklistValues"] if pv["active"]
        ]
    
    if field.get("referenceTo"):
        info["references"] = field["referenceTo"]
    
    return info

def print_object_summary(description: dict):
    """Print a human-readable summary of an object."""
    print(f"\n{'='*60}")
    print(f"Object: {description['name']} ({description['label']})")
    print(f"{'='*60}")
    
    fields = description["fields"]
    
    # Required fields
    required = [f for f in fields if not f["nillable"] and not f["defaultedOnCreate"] and f["createable"]]
    if required:
        print("\nREQUIRED FIELDS (must provide on create):")
        for f in required:
            print(f"  - {f['name']} ({f['type']}): {f['label']}")
    
    # Picklist fields
    picklists = [f for f in fields if f["type"] == "picklist" and f.get("picklistValues")]
    if picklists:
        print("\nPICKLIST FIELDS:")
        for f in picklists:
            active_values = [pv["value"] for pv in f["picklistValues"] if pv["active"]]
            print(f"  - {f['name']}: {f['label']}")
            for v in active_values[:10]:
                print(f"      * {v}")
            if len(active_values) > 10:
                print(f"      ... and {len(active_values) - 10} more")
    
    # Reference fields
    refs = [f for f in fields if f.get("referenceTo")]
    if refs:
        print("\nREFERENCE FIELDS:")
        for f in refs:
            print(f"  - {f['name']} -> {', '.join(f['referenceTo'])}")
    
    # All createable fields
    createable = [f for f in fields if f["createable"]]
    print(f"\nALL CREATEABLE FIELDS ({len(createable)} total):")
    for f in sorted(createable, key=lambda x: x["name"]):
        req = "*" if not f["nillable"] and not f["defaultedOnCreate"] else " "
        print(f"  {req} {f['name']:40} {f['type']:15} {f['label']}")

def main():
    parser = argparse.ArgumentParser(description="Describe Salesforce objects")
    parser.add_argument("objects", nargs="+", help="Object names to describe (e.g., Lead Account)")
    parser.add_argument("--output", "-o", help="Output file for JSON (optional)")
    parser.add_argument("--json", action="store_true", help="Output as JSON only")
    args = parser.parse_args()
    
    base_url = get_env_or_exit("SF_BASE_URL")
    api_version = os.environ.get("SF_API_VERSION", "v59.0")
    token = get_access_token()
    
    results = {}
    for obj_name in args.objects:
        try:
            desc = describe_object(base_url, token, obj_name, api_version)
            results[obj_name] = {
                "name": desc["name"],
                "label": desc["label"],
                "fields": [format_field_info(f) for f in desc["fields"]],
            }
            if not args.json:
                print_object_summary(desc)
        except requests.HTTPError as e:
            print(f"Error describing {obj_name}: {e}", file=sys.stderr)
    
    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nSchema saved to {args.output}")
    
    if args.json:
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
