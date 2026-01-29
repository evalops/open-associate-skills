#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse
from urllib.parse import urljoin

import requests


def get_env(name: str, required: bool = True, default: str | None = None) -> str | None:
    val = os.getenv(name, default)
    if required and not val:
        print(f"Missing required env var: {name}", file=sys.stderr)
        sys.exit(2)
    return val


def main() -> None:
    parser = argparse.ArgumentParser(description="Get a Salesforce access token using OAuth client credentials flow.")
    parser.add_argument("--base-url", default=os.getenv("SF_BASE_URL"), help="Salesforce base URL, e.g. https://yourdomain.my.salesforce.com")
    parser.add_argument("--client-id", default=os.getenv("SF_CLIENT_ID"))
    parser.add_argument("--client-secret", default=os.getenv("SF_CLIENT_SECRET"))
    parser.add_argument("--token-endpoint", default=None, help="Override token endpoint; defaults to <base-url>/services/oauth2/token")
    args = parser.parse_args()

    base_url = args.base_url
    if not base_url:
        print("SF_BASE_URL is required (or pass --base-url).", file=sys.stderr)
        sys.exit(2)

    client_id = args.client_id or get_env("SF_CLIENT_ID")
    client_secret = args.client_secret or get_env("SF_CLIENT_SECRET")

    token_url = args.token_endpoint or urljoin(base_url.rstrip("/") + "/", "services/oauth2/token")

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    resp = requests.post(token_url, data=data, timeout=30)
    if resp.status_code >= 400:
        print(f"Token request failed: {resp.status_code}", file=sys.stderr)
        print(resp.text, file=sys.stderr)
        sys.exit(1)

    payload = resp.json()
    # Print token to stdout as JSON for piping into other scripts
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
