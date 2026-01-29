#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse
from urllib.parse import quote_plus

import requests


def env(name: str, default: str | None = None, required: bool = True) -> str:
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
    r = requests.post(url, headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"}, data=json.dumps(fields), timeout=30)
    if r.status_code >= 400:
        raise RuntimeError(f"Create Lead failed ({r.status_code}): {r.text}")
    return r.json().get("id")


def update_lead(lead_id: str, fields: dict) -> None:
    url = f"{base_url()}/services/data/{api_version()}/sobjects/Lead/{lead_id}"
    r = requests.patch(url, headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"}, data=json.dumps(fields), timeout=30)
    if r.status_code >= 400:
        raise RuntimeError(f"Update Lead failed ({r.status_code}): {r.text}")


def main() -> None:
    p = argparse.ArgumentParser(description="Upsert a Salesforce Lead by email.")
    p.add_argument("--email", required=True)
    p.add_argument("--first", required=True)
    p.add_argument("--last", required=True)
    p.add_argument("--company", required=True)
    p.add_argument("--title", default=None)
    p.add_argument("--website", default=None)
    p.add_argument("--status", default="Open - Not Contacted")
    args = p.parse_args()

    email = args.email.replace("'", "\'")
    result = soql_query(f"SELECT Id FROM Lead WHERE Email='{email}' LIMIT 1")
    records = result.get("records", [])
    fields = {
        "FirstName": args.first,
        "LastName": args.last,
        "Company": args.company,
        "Email": args.email,
        "Status": args.status,
    }
    if args.title:
        fields["Title"] = args.title
    if args.website:
        fields["Website"] = args.website

    if records:
        lead_id = records[0]["Id"]
        update_lead(lead_id, fields)
        print(json.dumps({"action": "updated", "id": lead_id}, indent=2))
    else:
        lead_id = create_lead(fields)
        print(json.dumps({"action": "created", "id": lead_id}, indent=2))


if __name__ == "__main__":
    main()
