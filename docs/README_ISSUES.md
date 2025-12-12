Quick notes: how to create the drafted issues

1. To list the prepared issues, open `ISSUES_TO_CREATE.md`.
2. To auto-create them on GitHub:

```bash
export GITHUB_TOKEN=ghp_xxx   # token with repo:issues
python3 scripts/create_issues.py --owner cpgoswami550-del --repo skills-integrate-mcp-with-copilot
```

3. If you prefer, create issues manually by copying titles/bodies from `ISSUES_TO_CREATE.md` into GitHub Issues.
