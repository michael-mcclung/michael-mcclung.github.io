# Test results — michael-mcclung.github.io

**Renovation under test:** branch `renovation/portfolio-2026` @ `c25c2f7f3a730e9c9647788c1bfab7e1ff277733`  
**Working copy:** `/workspace/personal-site`  
**Recovery tag:** `pre-renovation-2026-10-29` (`fda53c8`)  
**Timezone:** America/Chicago (UTC-5)

Do not invent scores. Production rows stay pending until merge + Pages deploy.

---

## 1. Build

| Check | Tool / command | Result | Notes |
|-------|----------------|--------|-------|
| Local static build | `python3 scripts/build_static.py` | **pass** (Documentation Specialist, Oct 29, 2026 CT) | Built `_site` for four pages + copied assets |
| Jekyll / Pages CI build | `actions/jekyll-build-pages` / quality workflow | not yet measured (pending merge) | Workflow present on branch |
| Site security workflow | `site-security-check.yml` | not yet measured (pending merge) | |
| Site quality workflow | `site-quality-check.yml` | not yet measured (pending merge) | html-proofer + lychee configured |

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

### 2c. Production (live GitHub Pages)

| Check | Result |
|-------|--------|
| All production URL / asset checks after merge | **not yet measured (pending merge)** |

---

## 3. Responsive sizes

| Viewport | Width × height (CSS px) | Result | Notes |
|----------|-------------------------|--------|-------|
| Mobile | 375 × 812 (example) | not yet measured | |
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

Lighthouse **accessibility** scores for home are under §5 (SE).

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
| Lighthouse version | not stated in branch files (unknown) |
| URL tested | Local home page (SE) |
| Date / time (CT) | Oct 29, 2026 |
| Other routes | **not measured** — home page only |
| Production Lighthouse | **not yet measured (pending merge)** |

Documentation Specialist did **not** re-run Lighthouse; scores above are attributed to the Software Engineer as requested.

---

## 6. Sign-off

| Role | Name / note | Date (CT) | Outcome |
|------|-------------|-----------|---------|
| Software Engineer | Local links, PDF, HTML validation; Lighthouse home 93/100/100/100 (mobile) and 99/100/100/100 (desktop) | Oct 29, 2026 | Reported pass |
| Documentation Specialist | Local `_site` HTTP inventory + PDF validity | Oct 29, 2026 | Internal local links + PDF pass; LinkedIn not bot-checked; production pending merge |
| Independent reviewer | | | not yet measured (pending merge) |
