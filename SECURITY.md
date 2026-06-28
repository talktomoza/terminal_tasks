# GitHub Security Guide

## What Must NEVER Be Pushed to GitHub

The following types of sensitive information must **never** be committed or pushed to any repository — public or private:

| Category | Examples |
|---|---|
| API Keys | `OPENAI_API_KEY`, `STRIPE_SECRET_KEY`, `GOOGLE_API_KEY` |
| Private Keys | SSH private keys (`id_rsa`), SSL/TLS private keys (`.pem`) |
| Database Credentials | Usernames, passwords, connection strings |
| Environment Variables | `.env` files containing any secrets |
| OAuth Tokens | Access tokens, refresh tokens |
| Cloud Credentials | AWS `credentials` file, GCP service account JSON |

---

## Public vs Private Repositories

### Public Repository
- **Visible to everyone** on the internet — including search engines and bots.
- Anyone can view, clone, and fork your code.
- **Never store secrets here**, even temporarily. Bots actively scan GitHub for exposed credentials within seconds of a push.

### Private Repository
- Only accessible to you and explicitly invited collaborators.
- Safer for internal or sensitive projects, but **still not a safe place for secrets**.
- Former collaborators, accidental public conversions, or data breaches can expose secrets.

> **Rule of thumb:** Treat every repository as if it will be public one day.

---

## Common Vulnerabilities from Committed Secrets

1. **Credential Theft** — Attackers scrape GitHub for API keys and immediately abuse them (e.g., spin up expensive cloud VMs on your AWS account).
2. **Data Breaches** — Exposed database credentials give attackers direct access to user data.
3. **Account Takeover** — OAuth tokens let attackers impersonate your application or users.
4. **Financial Loss** — Leaked cloud keys can result in thousands of dollars in unauthorized usage.
5. **Reputational Damage** — A public breach erodes user trust permanently.

---

## Best Practices

### Use `.env` Files
Store secrets locally in a `.env` file and **never commit it**:
```
DATABASE_URL=postgres://user:password@localhost/mydb
SECRET_KEY=mysupersecretkey
```

### Always Add `.env` to `.gitignore`
```
# .gitignore
.env
.env.local
.env.production
```

### Use Environment Variables in Code
```python
import os
db_url = os.getenv("DATABASE_URL")
```

### If a Secret Was Accidentally Pushed
1. **Revoke/rotate the key immediately** — assume it is compromised.
2. Remove it from the commit history using `git filter-branch` or BFG Repo Cleaner.
3. Force-push the cleaned history.
4. Notify affected services.

---

## Tools for Prevention
- [git-secrets](https://github.com/awslabs/git-secrets) — Prevents committing secrets automatically.
- [truffleHog](https://github.com/trufflesecurity/trufflehog) — Scans repos for exposed credentials.
- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning) — Built-in GitHub protection for public repos.
