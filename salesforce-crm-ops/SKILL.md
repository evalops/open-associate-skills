---
name: salesforce-crm-ops
description: Operate Salesforce as the VC associate CRM: authenticate via OAuth, query with SOQL, upsert Leads/Accounts, create Opportunities, and log Activities/Tasks for dealflow and portfolio support.
license: Proprietary
compatibility: Requires internet access and Salesforce REST API credentials; scripts require Python 3 + requests.
metadata:
  author: evalops
  version: "0.1"
---
# Salesforce CRM ops

## When to use
Use this skill when you need to:
- Create or update Leads/Accounts/Opportunities for dealflow
- Log meetings, diligence calls, and next steps as Activities/Tasks
- Query Salesforce for pipeline, duplicates, and coverage
- Automate basic CRM hygiene via scripts

## Compatibility / assumptions
This skill assumes:
- You have Salesforce REST API access and a Connected App.
- You can obtain an access token via OAuth (client credentials or another flow).
- You know your instance base URL (e.g., `https://yourdomain.my.salesforce.com`).

## Required environment variables (recommended)
Set:
- `SF_BASE_URL` (e.g., `https://yourdomain.my.salesforce.com`)
- `SF_CLIENT_ID`
- `SF_CLIENT_SECRET`

Optional:
- `SF_API_VERSION` (default `v59.0` if omitted)
- `SF_ACCESS_TOKEN` (if you already have one)

## Core workflows

### 1) Get an access token (OAuth client credentials)
Preferred for server-to-server integrations:
- POST to: `https://<mydomain>.my.salesforce.com/services/oauth2/token`
- Use grant type `client_credentials` (or whatever your org allows)

If your org uses a different OAuth flow, adapt accordingly.

### 2) Query Salesforce (SOQL)
Use the Query resource:
- `GET /services/data/vXX.X/query/?q=<SOQL>`

Reminder: encode spaces as `+` or `%20` in URLs.

### 3) Upsert / create a Lead
Common pattern:
1) Query by email to see if Lead exists
2) If exists, PATCH it
3) Else, POST a new Lead

### 4) Create an Opportunity for a deal
Minimum fields depend on your org, but commonly:
- Name
- StageName
- CloseDate

### 5) Log Activities / Tasks
Create a Task:
- Subject
- WhatId (Account/Opportunity)
- WhoId (Lead/Contact)
- ActivityDate (due date)
- Status

## Scripts
This skill includes reference scripts you can run.

- scripts/sf_oauth_client_credentials.py
- scripts/sf_query.py
- scripts/sf_upsert_lead.py
- scripts/sf_create_opportunity.py
- scripts/sf_create_task.py

## Safety / hygiene rules
- Prefer upsert by stable identifiers (email, domain) to avoid duplicates.
- Keep notes factual (assume audits).
- Record next step with a due date; otherwise the CRM is dead.

## Examples

### Get token
```bash
python3 scripts/sf_oauth_client_credentials.py
```

### Query leads by email
```bash
python3 scripts/sf_query.py "SELECT Id, Name, Email, Company FROM Lead WHERE Email='founder@company.com' LIMIT 5"
```

### Upsert a lead
```bash
python3 scripts/sf_upsert_lead.py --email founder@company.com --first "Ada" --last "Lovelace" --company "ExampleAI" --title "CEO" --website "https://example.ai" --status "Open - Not Contacted"
```

### Create an opportunity
```bash
python3 scripts/sf_create_opportunity.py --name "ExampleAI Seed" --stage "Qualification" --close-date "2026-03-31"
```
