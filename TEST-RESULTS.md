# Test results — michael-mcclung.github.io

**Renovation measured locally:** branch `renovation/portfolio-2026` @ `c25c2f7f3a730e9c9647788c1bfab7e1ff277733`  
**Working copy (local checks, Oct 29, 2026):** `/workspace/personal-site`  
**Production:** `master` after PR #3 (`1a36f4f`, Oct 29, 2026). Tip at the Oct 30, 2026 production check: `8b396d5` (PR #4). Live: https://michael-mcclung.github.io/  
**Recovery tag:** `pre-renovation-2026-10-29` (`fda53c8`)  
**Timezone:** America/Chicago (UTC-5)

Do not invent scores. A row stays **not yet measured** unless a run result or a live check is recorded below.

---

## 1. Build

| Check | Tool / command | Result | Notes |
|-------|----------------|--------|-------|
| Local static build | `python3 scripts/build_static.py` | **pass** (Documentation Specialist, Oct 29, 2026 CT) | Built `_site` for four pages + copied assets |
| Jekyll / Pages CI build | Build and deploy Jekyll site to GitHub Pages (`actions/jekyll-build-pages`, then deploy) | **pass** | `gh run view` on master after `1a36f4f`: [run 40995014943](https://github.com/michael-mcclung/michael-mcclung.github.io/actions/runs/40995014943) (`2026-10-30T03:01:34Z`), jobs `build` and `deploy` success. Also **pass** on `8b396d5`: [run 41030632077](https://github.com/michael-mcclung/michael-mcclung.github.io/actions/runs/41030632077) (`2026-10-30T09:03:23Z`), jobs `build` and `deploy` success. Step logs were not re-read. |
| Site security workflow | `site-security-check.yml` | **pass** | [run 40995015017](https://github.com/michael-mcclung/michael-mcclung.github.io/actions/runs/40995015017) on `1a36f4f` (`2026-10-30T03:01:34Z`), job `validate-site` success. Also **pass** on `8b396d5`: [run 41030632220](https://github.com/michael-mcclung/michael-mcclung.github.io/actions/runs/41030632220) (`2026-10-30T09:03:23Z`), job `validate-site` success. |
| Site quality workflow | `site-quality-check.yml` | **pass** | [run 40995014932](https://github.com/michael-mcclung/michael-mcclung.github.io/actions/runs/40995014932) on `1a36f4f` (`2026-10-30T03:01:34Z`), job `validate` success. Also **pass** on `8b396d5`: [run 41030632253](https://github.com/michael-mcclung/michael-mcclung.github.io/actions/runs/41030632253) (`2026-10-30T09:03:23Z`), job `validate` success. Step logs were not re-read. |

**Software Engineer (Oct 29, 2026):** reported local links, PDF download, and HTML validation **passed** on the renovation branch (recorded here as SE attestation; not re-run by Docs except local HTTP checks below).

---

## 2. Link checks

### 2a. Documentation Specialist — local `_site` (Oct 29, 2026 CT)

Method: `python3 scripts/build_static.py` then `python3 -m http.server 8765` in `_site`; `curl` to `http://127.0.0.1:8765…`.

| URL (local) | Status | Pass? | Notes |
|-------------|--------|-------|-------|
| `/` | 200 | yes | Home ~17 KB |
| `/index.html` | 200 | yes | |
| `/main/journey/` | 200 | yes | |
| `/main/journey/index.html` | 200 | yes | |
| `/main/projects/` | 200 | yes | |
| `/main/projects/index.html` | 200 | yes | |
| `/main/resume/` | 200 | yes | |
| `/main/resume/index.html` | 200 | yes | |
| `/assets/resume/Michael-McClung-Resume-2025.pdf` | 200 | yes | 96 534 bytes; `%PDF` + `%%EOF` |
| `/assets/css/site.css` | 200 | yes | |
| `/assets/js/site.js` | 200 | yes | |
| `/assets/img/portrait.jpg` | 200 | yes | |
| `/assets/img/favicon.svg` | 200 | yes | |
| `/robots.txt` | 200 | yes | |
| `/sitemap.xml` | 200 | yes | |

Home content smoke: title contains `Michael McClung | Full Stack Software Engineer`; H1 `Michael McClung`; role + subline strings present.

External GitHub / RollWithDFW / CDN not re-curled in this follow-up (file hrefs verified in source). **LinkedIn:** not bot-checked (cannot be reliably automated).

### 2b. Software Engineer attestation (Oct 29, 2026)

| Check | Result |
|-------|--------|
| Local links | passed (per SE) |
| PDF download | passed (per SE) |
| HTML validation | passed (per SE) |
| LinkedIn | cannot be bot-checked |

### 2c. Production (live GitHub Pages) — Oct 30, 2026

Method: HTTP GET (Python `urllib`) of each internal URL on https://michael-mcclung.github.io. Same-host links were taken from the HTML of `/`, `/main/journey/`, `/main/projects/`, and `/main/resume/`, plus `robots.txt` and `sitemap.xml`. **LinkedIn was not requested** (not bot-checked). External hosts (GitHub, Google Fonts, rollwithdfw.com) were not requested.

| URL | Status | Pass? | Notes |
|-----|--------|-------|-------|
| `https://michael-mcclung.github.io/` | 200 | yes | `text/html`, 17 517 bytes |
| `https://michael-mcclung.github.io` | 200 | yes | same document as `/` |
| `https://michael-mcclung.github.io/index.html` | 200 | yes | `text/html`, 17 517 bytes |
| `https://michael-mcclung.github.io/main/journey/` | 200 | yes | `text/html`, 8 587 bytes |
| `https://michael-mcclung.github.io/main/journey/index.html` | 200 | yes | `text/html`, 8 587 bytes |
| `https://michael-mcclung.github.io/main/projects/` | 200 | yes | `text/html`, 7 956 bytes |
| `https://michael-mcclung.github.io/main/projects/index.html` | 200 | yes | `text/html`, 7 956 bytes |
| `https://michael-mcclung.github.io/main/resume/` | 200 | yes | `text/html`, 12 435 bytes |
| `https://michael-mcclung.github.io/main/resume/index.html` | 200 | yes | `text/html`, 12 435 bytes |
| `https://michael-mcclung.github.io/assets/resume/Michael-McClung-Resume-2025.pdf` | 200 | yes | `application/pdf`, 96 534 bytes; starts with `%PDF-1.4`; `%%EOF` in the last 64 bytes |
| `https://michael-mcclung.github.io/assets/css/site.css` | 200 | yes | `text/css`, 14 167 bytes |
| `https://michael-mcclung.github.io/assets/js/site.js` | 200 | yes | `application/javascript`, 1 429 bytes |
| `https://michael-mcclung.github.io/assets/img/portrait.jpg` | 200 | yes | `image/jpeg`, 73 637 bytes |
| `https://michael-mcclung.github.io/assets/img/favicon.svg` | 200 | yes | `image/svg+xml`, 388 bytes |
| `https://michael-mcclung.github.io/robots.txt` | 200 | yes | `text/plain`, 79 bytes |
| `https://michael-mcclung.github.io/sitemap.xml` | 200 | yes | `application/xml`, 769 bytes |

LinkedIn: **not bot-checked**.

---

## 3. Responsive sizes

| Viewport | Width × height (CSS px) | Result | Notes |
|----------|-------------------------|--------|-------|
| Mobile | 375 | **PASS** (team-reported) | Software Engineer, manual check of the live site https://michael-mcclung.github.io/ on Oct 29, 2026 at about 10:04 PM CT. Layout was clean with no horizontal overflow. Not re-measured in this change. |
| Tablet | 768 × 1024 (example) | not yet measured | |
| Desktop | 1440 × 900 (example) | not yet measured | |

Branch CSS includes mobile nav + responsive rules; visual pass not separately scored here.

---

## 4. Accessibility

| Check | Tool | Result | Notes |
|-------|------|--------|-------|
| Automated a11y beyond Lighthouse a11y category | not yet measured | not yet measured | Skip link + `aria-*` present in markup |
| Keyboard nav | not yet measured | not yet measured | |
| Screen reader smoke | not yet measured | not yet measured | |

Lighthouse **accessibility** scores for the home page (local and live production) are under §5.

---

## 5. Lighthouse (home page)

**Software Engineer measured** on the **home page**, served **locally** (Oct 29, 2026). Categories: Performance / Accessibility / Best practices / SEO.

| Category | Mobile | Desktop | Notes |
|----------|--------|---------|-------|
| Performance | **93** | **99** | SE, local home only |
| Accessibility | **100** | **100** | SE, local home only |
| Best practices | **100** | **100** | SE, local home only |
| SEO | **100** | **100** | SE, local home only |

| Meta | Value |
|------|--------|
| Lighthouse version | not stated (unknown) |
| URL tested (local) | Local home page (SE) |
| Date / time (CT) | Oct 29, 2026 |
| Other routes | **not measured** — home page only |
| Production Lighthouse | **measured** Oct 29, 2026, live home page. Source: live Lighthouse on the home page. Mobile Performance 93, Accessibility 100, Best Practices 100, SEO 100. Desktop 99 / 100 / 100 / 100. This docs sync did not re-run Lighthouse. |

Production home page (live), Oct 29, 2026:

| Category | Mobile | Desktop | Notes |
|----------|--------|---------|-------|
| Performance | **93** | **99** | Live home page only |
| Accessibility | **100** | **100** | Live home page only |
| Best practices | **100** | **100** | Live home page only |
| SEO | **100** | **100** | Live home page only |

Documentation Specialist did **not** re-run Lighthouse. The local table is the Software Engineer’s local home-page run. The production table is the stated live measurement (Oct 29, 2026). Lighthouse version for the production run: **not stated** (unknown). Other routes: **not measured**.

---

## 6. Sign-off

| Role | Name / note | Date (CT) | Outcome |
|------|-------------|-----------|---------|
| Software Engineer | Local links, PDF, HTML validation; Lighthouse home 93/100/100/100 (mobile) and 99/100/100/100 (desktop) | Oct 29, 2026 | Reported pass |
| Documentation Specialist | Local `_site` HTTP inventory + PDF validity | Oct 29, 2026 | Internal local links + PDF pass; LinkedIn not bot-checked; production not measured that day |
| Docs sync | Actions conclusions on master after `1a36f4f` and on `8b396d5`; live internal HTTP + PDF; production home-page Lighthouse recorded from the Oct 29, 2026 live measurement | Oct 30, 2026 | See §1, §2c, and §5. LinkedIn not bot-checked. |
| Independent reviewer | Chief of Staff reviewed PR #3 and checked the facts, the contact links, the 7 repo links, the real Jekyll build, and the rollback tag `pre-renovation-2026-10-29` | Oct 29, 2026, 9:41 PM CT | **PASS** (team-reported) |
