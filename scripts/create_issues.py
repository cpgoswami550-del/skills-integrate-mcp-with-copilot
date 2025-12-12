#!/usr/bin/env python3
"""
Create the prepared issues in ISSUES_TO_CREATE.md as GitHub issues.

Usage:
  export GITHUB_TOKEN=ghp_...   # token with repo:issues
  python3 scripts/create_issues.py --owner cpgoswami550-del --repo skills-integrate-mcp-with-copilot

The script posts the 12 prepared issues built into this script.
"""
import os
import sys
import requests
import argparse

ISSUES = [
    {
        "title": "Add persistent storage (SQLite) for activities",
        "body": "Problem: Current activities are in-memory and lost on restart.\n\nProposed: Add SQLite + ORM models and migrations for activities and participants; swap in DB-backed CRUD for existing endpoints.\n\nAcceptance criteria:\n- Activity and Participant models with migrations exist.\n- GET /activities, POST /activities/{name}/signup, DELETE /activities/{name}/unregister use DB.\n- Tests for signup/unregister are added.\n",
        "labels": ["enhancement","backend"]
    },
    {
        "title": "Add user authentication (email-based) and basic ACL",
        "body": "Problem: No authentication or roles; anyone can sign up students.\n\nProposed: Implement simple auth (FastAPI OAuth2 password flow), add roles: admin, teacher, student. Protect admin endpoints.\n\nAcceptance criteria:\n- Login/register endpoints.\n- Admin-only endpoints protected.\n- Seed an admin user for local dev.\n",
        "labels": ["enhancement","auth"]
    },
    {
        "title": "User management UI & API",
        "body": "Add endpoints + minimal admin UI to list users, create/edit users and assign roles.\n\nAcceptance criteria: CRUD API for users and a new static admin page under /static/admin_users.html.\n",
        "labels": ["frontend","backend"]
    },
    {
        "title": "Membership/Subscription support (plans & signup caps)",
        "body": "Introduce Plan/Membership concept and ability to attach plans to activities (e.g., paid clubs, priority signups).\n\nAcceptance criteria: Plan model, admin APIs for plans, activity->plan association.\n",
        "labels": ["feature","data-model"]
    },
    {
        "title": "Billing & invoices (optional)",
        "body": "Implement invoices for paid activities, store payments, invoice numbers, and seed invoice settings.\n\nAcceptance criteria: Invoice model, payment endpoints (mock), invoice numbering configuration.\n",
        "labels": ["optional","billing"]
    },
    {
        "title": "Dashboard & reporting",
        "body": "Add a simple admin dashboard showing counts: total activities, registrations this month, full activities, upcoming schedules.\n\nAcceptance: New /static/admin_dashboard.html plus API endpoints to provide metrics.\n",
        "labels": ["frontend","reporting"]
    },
    {
        "title": "SMS/email notifications for signups",
        "body": "Integrate optional SMS/email notifications for signup confirmations and reminders (configurable).\n\nAcceptance: Configurable provider, mock provider for dev, endpoints to trigger notifications.\n",
        "labels": ["integration","notifications"]
    },
    {
        "title": "Media (profile images) support",
        "body": "Allow users to upload profile images and serve via static path; integrate storage in static/uploads.\n\nAcceptance: Upload API, storage, and display in admin user list.\n",
        "labels": ["feature","media"]
    },
    {
        "title": "Scheduler (cron) for reminders and cleanup",
        "body": "Add scheduled tasks (e.g., cleanup stale signups, send reminders) using APScheduler or FastAPI background tasks + cron setup doc.\n\nAcceptance: Scheduler service and docs to enable cron.\n",
        "labels": ["infra","scheduler"]
    },
    {
        "title": "Logging, error monitoring, and debug tooling",
        "body": "Add structured logging, Sentry integration optional, and a debug mode setting.\n\nAcceptance: Configurable logging and Sentry env var usage.\n",
        "labels": ["ops","logging"]
    },
    {
        "title": "Tests and seed data",
        "body": "Add unit tests for core signup flows and fixtures/seeds for demo data.\n\nAcceptance: pytest setup, tests/ with signup/unregister tests, and a seed script.\n",
        "labels": ["tests"]
    },
    {
        "title": "Docs & install guide update",
        "body": "Update README.md with new setup steps: DB migrations, env vars, running scheduler, and demo credentials.\n\nAcceptance: Clear run instructions and example .env.\n",
        "labels": ["docs"]
    }
]


def create_issue(owner, repo, token, issue):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    payload = {"title": issue["title"], "body": issue["body"], "labels": issue.get("labels", [])}
    r = requests.post(url, json=payload, headers=headers)
    if r.status_code in (200,201):
        data = r.json()
        print(f"Created: {data['html_url']}")
    else:
        print(f"Failed to create issue '{issue['title']}': {r.status_code} {r.text}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--owner", required=True)
    p.add_argument("--repo", required=True)
    p.add_argument("--token", default=os.getenv("GITHUB_TOKEN"))
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    if not args.token and not args.dry_run:
        print("Error: Provide a GitHub token via --token or GITHUB_TOKEN env var.")
        sys.exit(1)

    for issue in ISSUES:
        print("\n---\n")
        print(f"Title: {issue['title']}")
        if args.dry_run:
            print(issue['body'])
            continue
        create_issue(args.owner, args.repo, args.token, issue)


if __name__ == '__main__':
    main()
