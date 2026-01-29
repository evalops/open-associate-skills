#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse
from urllib.parse import quote_plus, urljoin

import requests


def get_api_version() -> str:
    return os.getenv("SF_API_VERSION", "v59.0")


def get_base_url() -> str:
    base = os.getenv("SF_BASE_URL")
    if not base:
        print("Missing SF_BASE_URL", file=sys.stderr)
        sys.exit(2)
    return base.rstrip("/")


def get_token() -> str:
    token = os.getenv("SF_ACCESS_TOKEN")
    if not token:
        print("Missing SF_ACCESS_TOKEN (set it, or run sf_oauth_client_credentials.py and export access_token).", file=sys.stderr)
        sys.exit(2)
    return token


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a SOQL query via Salesforce REST API and print results.")
    parser.add_argument("soql", help="SOQL query string, e.g. SELECT Id, Name FROM Lead LIMIT 5")
    args = parser.parse_args()

    base_url = get_base_url()
    token = get_token()
    api_version = get_api_version()

    q = quote_plus(args.soql)
    path = f"/services/data/{api_version}/query/?q={q}"
    url = base_url + path

    resp = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=30)
    if resp.status_code >= 400:
        print(f"Query failed: {resp.status_code}", file=sys.stderr)
        print(resp.text, file=sys.stderr)
        sys.exit(1)

    print(json.dumps(resp.json(), indent=2))


if __name__ == "__main__":
    main()
