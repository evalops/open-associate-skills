#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse
import datetime

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


def main() -> None:
    p = argparse.ArgumentParser(description="Create a Salesforce Opportunity.")
    p.add_argument("--name", required=True)
    p.add_argument("--stage", required=True, help="StageName value in your org, e.g. Qualification")
    p.add_argument("--close-date", required=True, help="YYYY-MM-DD")
    p.add_argument("--account-id", default=None, help="Optional AccountId to link")
    p.add_argument("--amount", default=None, help="Optional numeric Amount")
    args = p.parse_args()

    # basic validation
    datetime.date.fromisoformat(args.close_date)

    fields = {"Name": args.name, "StageName": args.stage, "CloseDate": args.close_date}
    if args.account_id:
        fields["AccountId"] = args.account_id
    if args.amount is not None:
        try:
            fields["Amount"] = float(args.amount)
        except ValueError:
            print("Amount must be numeric.", file=sys.stderr)
            sys.exit(2)

    url = f"{base_url()}/services/data/{api_version()}/sobjects/Opportunity/"
    r = requests.post(url, headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"}, data=json.dumps(fields), timeout=30)
    if r.status_code >= 400:
        print(f"Create Opportunity failed ({r.status_code}): {r.text}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(r.json(), indent=2))


if __name__ == "__main__":
    main()
