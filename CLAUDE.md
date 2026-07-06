# LuxAed — project rules (read every session)

LuxAed (luxaed.ee) is a **fence & gate** company in Tallinn/Harjumaa. This repo is the
LuxAed website: a trilingual static site (ET root, RU at `/ru/`, EN at `/en/`), built by
Python generators and deployed to Vercel on the `luxaed.ee` domain.

## ⛔ HARD RULE #1 — moving24 is a SEPARATE company. Two different sites. Never mix them.

`reference-kit/` is a **local-only copy of moving24.ee**, kept purely as a design/copy
reference. moving24 is a *different business*. Treat it like a read-only textbook:

- **NEVER deploy anything from `reference-kit/`.** It must stay excluded in `.vercelignore`.
  Before every push/deploy, confirm `.vercelignore` still lists `reference-kit`.
- **NEVER edit moving24.ee or its files** — only read from `reference-kit/` to copy design
  patterns into LuxAed's own files. Copy, don't reinvent; but the output is always LuxAed's.
- **NEVER let the string "moving24" appear in any shipped file** (html/css/js/py that gets
  deployed, or user-visible text, comments included). It may exist ONLY inside `reference-kit/`.
- The name "moving24" must not appear in filenames, folder names, `.gitignore`, or comments
  outside `reference-kit/`.

### Why this rule exists (a real incident)
The reference copy was once named `moving24-template/` and had NO `.vercelignore`, so Vercel
**publicly served the entire moving24 site + internal guides on luxaed.ee**
(`/moving24-template/site/` → 200, `/GUIDE.md` → 200, `/build_pages.py` → 200). That is a
competitor's whole site leaking on our domain. Fixed by: renaming to `reference-kit/`, adding
`.vercelignore` (excludes `reference-kit`, `*.py`, `*.md`, generators), verified 404 on live.

### Deploy checklist (run before every deploy)
1. `.vercelignore` excludes: `reference-kit`, `*.py`, `__pycache__`, `*.md`, generators.
2. `grep -rIl moving24 . --exclude-dir=reference-kit --exclude-dir=.git` → **must be empty.**
3. After deploy, curl-verify these return **404**: `/reference-kit/`, `/build_pages.py`.

## Build & deploy
- Edit content in the `gen_*.py` generators + `build_pages.py`, then run `python3 apply_base.py`
  (adds path prefix + CSS cache-bust). `BASE=""` for the root-domain deploy.
- Push to `main` → Vercel auto-deploys. Static files + `api/lead.js` (serverless) go live.

## Lead form email
- `api/lead.js` = Vercel serverless: nodemailer → **Gmail SMTP (port 465) + App Password**.
  This mirrors how moving24 does it (PHPMailer + Gmail SMTP + App Password in `config.php`) —
  it is NOT the Gmail API, just SMTP with an app password.
- **Secrets NEVER go in code.** The App Password lives ONLY in Vercel → Settings →
  Environment Variables: `GMAIL_USER`, `GMAIL_APP_PASSWORD`, `LEAD_TO`. Code reads
  `process.env.*`. Without them the form still returns ok (email skipped).
