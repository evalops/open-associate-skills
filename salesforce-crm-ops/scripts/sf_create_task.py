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
    p = argparse.ArgumentParser(description="Create a Salesforce Task.")
    p.add_argument("--subject", required=True)
    p.add_argument("--due", required=True, help="YYYY-MM-DD")
    p.add_argument("--what-id", default=None, help="Related record ID (Opportunity/Account)")
    p.add_argument("--who-id", default=None, help="Name record ID (Lead/Contact)")
    p.add_argument("--status", default="Not Started")
    p.add_argument("--priority", default="Normal")
    p.add_argument("--comments", default=None)
    args = p.parse_args()

    datetime.date.fromisoformat(args.due)

    fields = {
        "Subject": args.subject,
        "ActivityDate": args.due,
        "Status": args.status,
        "Priority": args.priority,
    }
    if args.what_id:
        fields["WhatId"] = args.what_id
    if args.who_id:
        fields["WhoId"] = args.who_id
    if args.comments:
        fields["Description"] = args.comments

    url = f"{base_url()}/services/data/{api_version()}/sobjects/Task/"
    r = requests.post(url, headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"}, data=json.dumps(fields), timeout=30)
    if r.status_code >= 400:
        print(f"Create Task failed ({r.status_code}): {r.text}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(r.json(), indent=2))


if __name__ == "__main__":
    main()
