# git_security

## Purpose
A security audit and documentation repository covering best practices for keeping sensitive data out of version control.

## Contents
- `SECURITY.md` — What to never push, common vulnerabilities, and best practices.
- `.gitignore` — A comprehensive template to exclude sensitive files from Git tracking.

## Key Lesson
> Never commit secrets. Not in public repos. Not in private repos. Not "just for now."

Always use environment variables and `.env` files — and always add them to `.gitignore`.
