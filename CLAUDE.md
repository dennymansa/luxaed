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

## Current buyer-guide architecture (2026-08-24)
- 17 complete ET/RU/EN hreflang groups and 51 canonical URLs in `sitemap.xml`.
- Buyer guides: `/hinnad/`, `/kuidas-valida-aeda/`, `/piirkonnad/harjumaa/` plus RU/EN counterparts.
- Intercom service: `/varavad/domofonid/`, `/ru/domofony-videodomofony/`, `/en/intercoms-video-intercoms/`. It covers outdoor panels, indoor/mobile control, PIN/RFID access and pedestrian-gate electric locks. Do not claim that a standard electric strike physically moves the gate; motorised opening requires a separate drive and safety design.
- Qualify video-intercom mobile and recording features by model, network and storage. Keep camera coverage focused on the owner's entrance, never promise filming a neighbour's property, and do not present continuous audio recording as part of video surveillance.
- Keep intercom page copy short and conversational. Lead with real-life uses such as welcoming guests, speaking to couriers, family access, remote opening and reviewing recorded events. Avoid technical phrases such as "send the lock a release command" in customer-facing copy.
- Keep every service-page hero outcome-led and conversational. Start with the homeowner's situation, then name the material and installation details below the fold. The shared `OUTCOME_COPY`, `USE_CASES` and `EXTRA_FAQ` maps in `service_layout.py` are the canonical semantic layer for ET/RU/EN and cover privacy, wind, noise, slopes, pets, children, access, maintenance, repair and price questions without keyword stuffing.
- For material-led searches such as "profiled sheet for a fence", keep the natural material synonyms but immediately qualify the offer as measurement, supply and installation of a finished fence. LuxAed is a contractor, not a retail sheet-material shop.
- The shared gates cluster at `/varavad/`, `/ru/vorota-avtomatika/` and `/en/gates-automation/` targets commercial automatic-gate installation intent without separate doorway pages. Preserve the same canonical URLs and cover automatic gates, sliding and swing gates, gate automation installation, price, safety and controls naturally in each language.
- Core service area is Tallinn and Harjumaa only. Do not generate nationwide or thin city doorway pages without unique local proof.
- Published price ranges are provisional 2026 market guides pending owner verification; the free measurement and written quotation are authoritative.
- Customer-facing copy must sound direct and human. Avoid em dashes in prose and avoid phrases such as "realistic budget ranges" or "provisional market guides". En dashes remain acceptable only inside real numeric or calendar ranges such as `25–45 €/m`.
- Lead form requires service, name and phone. Email, address, photos and comment are optional. Preserve first-touch UTM/click IDs, `submission_id`, `generate_lead`, GTM and Google Ads phone-click tracking.
