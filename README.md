# Michael McClung — Personal Portfolio Website

Public portfolio for **Michael McClung** (Mac), Full Stack Software Engineer.  
**Purpose:** Mac’s software engineering job search — recruiters and hiring managers.

- **Live site (production until merge):** https://michael-mcclung.github.io  
- **Repository:** https://github.com/michael-mcclung/michael-mcclung.github.io  
- **Default branch:** `master`  
- **Renovation branch:** `renovation/portfolio-2026` (working copy audited at `/workspace/personal-site`, tip `c25c2f7`)  
- **Recovery tag:** `pre-renovation-2026-10-29` → `fda53c8546c14e156bf7a67419198bffd3aa1353`  
- **Project tracker:** [TASK 011: Personal Website renovation](https://app.notion.com/p/409f021b1428818ba525d1ef46bff93e)

This README describes the **renovated** site as verified from `renovation/portfolio-2026` (Oct 29, 2026, America/Chicago). Pre-merge production still matches `ARCHITECTURE-current.md` / tag `pre-renovation-2026-10-29` until the PR lands.

**Headline (as implemented):** H1 `Michael McClung`, role line `Full Stack Software Engineer`, supporting line `I build software that fixes real business operations.`

---

## Project overview

Static, accessible recruiter-focused portfolio: hero with Contact / Download Resume / LinkedIn CTAs on every page; About, Experience, Projects, Skills, résumé (HTML + PDF), and contact. Built with Jekyll Liquid includes, one consolidated CSS file, small vanilla JS, and GitHub Pages.

| Rollback reference | Value |
|--------------------|--------|
| Tag | `pre-renovation-2026-10-29` |
| SHA | `fda53c8546c14e156bf7a67419198bffd3aa1353` |
| Date | Aug 11, 2026, 1:12:23 PM CT |
| Message | Fix resume page and render resume directly |

Related docs in this package: `ARCHITECTURE-current.md` (pre-renovation audit), `ARCHITECTURE-proposed.md` (post-renovation), `CHANGELOG.md`, `TEST-RESULTS.md`.

---

## Tech stack (renovated)

| Layer | Choice |
|-------|--------|
| Markup | Static HTML + Jekyll Liquid includes (`{% include %}`) and YAML front matter (`title`) |
| Config | `_config.yml` — `theme: null`, `url: https://michael-mcclung.github.io`, `baseurl: ""`, `markdown: kramdown` |
| Layouts | None (`_layouts/` unused) |
| Styles | Single `assets/css/site.css` (~14 KB). **No Bootstrap** |
| Fonts | Google Fonts — Inter (400–800) |
| Scripts | `assets/js/site.js` — mobile nav toggle, scroll reveal (`prefers-reduced-motion` aware), dynamic footer year |
| SEO | Canonical + Open Graph + Twitter meta in `_includes/head.html`; `robots.txt`; `sitemap.xml`; SVG favicon |
| Build / deploy | GitHub Actions → `actions/jekyll-build-pages@v1` → `actions/deploy-pages@v4` |
| Local preview | `scripts/build_static.py` (Python 3, expands includes without Ruby) |
| Hosting | GitHub Pages at `*.github.io` (no `CNAME` in repo) |
| Cost | $0 — mailto contact, free fonts, no paid analytics/forms |

No `Gemfile` in repo; CI Jekyll comes from GitHub’s Pages action / quality workflow gem install.

---

## Local setup

### Prerequisites

- Git  
- Python 3 (recommended local preview)  
- Optional: Ruby + Jekyll (CI-faithful / `site-quality-check` parity)

### Clone and branch

```bash
git clone https://github.com/michael-mcclung/michael-mcclung.github.io.git
cd michael-mcclung.github.io
git fetch origin
git checkout renovation/portfolio-2026   # or master after merge
```

### Preferred local preview (no Ruby)

```bash
python3 scripts/build_static.py
cd _site && python3 -m http.server 8080
# open http://127.0.0.1:8080
```

### Jekyll (matches quality / Pages build more closely)

```bash
jekyll serve
# or, if a Gemfile is added later: bundle exec jekyll serve
```

`_site/` is gitignored.

---

## Site structure (renovated)

```
index.html                 Home — hero, about, experience, projects, skills, resume CTA, contact
main/journey/index.html    Experience (dedicated page)
main/projects/index.html   Projects (incl. RollWithDFW → rollwithdfw.com)
main/resume/index.html     HTML résumé (phone + print); PDF download links
assets/resume/Michael-McClung-Resume-2025.pdf   Valid PDF (~96 KB), served as static asset
assets/css/site.css
assets/js/site.js
assets/img/portrait.jpg
assets/img/favicon.svg
_includes/                 head.html, navbar.html, footer.html
robots.txt
sitemap.xml
scripts/build_static.py
.github/workflows/         deploy.yml, site-security-check.yml, site-quality-check.yml
README.md / CHANGELOG.md / SECURITY.md / .gitignore
```

### Pages and purpose

| Page | Path | Purpose |
|------|------|---------|
| Home | `/` | Job-search landing: headline, CTAs, about, experience summary, projects, skills, contact |
| Experience | `/main/journey/` | Fuller experience / education narrative |
| Projects | `/main/projects/` | Project cards with external links |
| Resume | `/main/resume/` | HTML résumé; phone; PDF download; print |

### How the resume PDF is served

- File: `assets/resume/Michael-McClung-Resume-2025.pdf` (checked in; valid `%PDF-1.4` with xref/EOF; ~96 534 bytes on the branch).  
- Linked via Jekyll `relative_url` as `/assets/resume/Michael-McClung-Resume-2025.pdf` with `download="Michael-McClung-Resume-2025.pdf"`.  
- Appears in homepage hero, page CTA bars, résumé page, and `sitemap.xml`.  
- The old broken `main/resume/2025 Resume .pdf` (60-byte stub) is **removed**.  
- HTML résumé remains available for screen readers / print; phone is on the résumé page (and PDF), not required in the global nav.

### CSS / JS

- **CSS:** only `site.css` linked from head (legacy `style.css` / `modern.css` / `portfolio.css` / `showcase-home.css` / `mainStyles.css` removed).  
- **JS:** only `site.js` from footer (`defer`). No Bootstrap CDN. CSP `script-src 'self'`; styles allow self + Google Fonts.

---

## Deployment (GitHub Pages)

Unchanged deploy path (do not retarget Pages settings for routine content work):

1. Merge or push to `master`, or run **Build and deploy Jekyll site to GitHub Pages** (`workflow_dispatch`).  
2. `.github/workflows/deploy.yml` → checkout → `configure-pages` → `jekyll-build-pages@v1` → `upload-pages-artifact` → `deploy-pages@v4`.  
3. Site: https://michael-mcclung.github.io  

### Workflows in `.github/workflows`

| Workflow | File | Role |
|----------|------|------|
| Build and deploy Jekyll site to GitHub Pages | `deploy.yml` | Production build/deploy on `master` |
| Site security check | `site-security-check.yml` | CSP / `SECURITY.md` / no `http://` in HTML/CSS/JS |
| Site quality check | `site-quality-check.yml` **(new)** | Jekyll build, html-proofer (internal), lychee (external; LinkedIn/fonts excluded, `fail: false`), security basics + PDF presence |

---

## Rollback

**Never force-push `master`.**

Recovery point: tag **`pre-renovation-2026-10-29`** (= `fda53c8`).

1. **Preferred:** Revert the renovation merge commit through a normal PR into `master`. Wait for Actions Pages deploy.  
2. **Alternate:** Restore tree from the tag and open a forward PR:

```bash
git checkout -b rollback/pre-renovation-2026-10-29
git checkout pre-renovation-2026-10-29 -- .
git commit -m "Rollback site content to pre-renovation-2026-10-29 (fda53c8)"
# push branch → open PR → merge to master → confirm live site
```

Update `CHANGELOG.md` with the new production SHA after any rollback.

---

## Maintenance

### Public contact (Mac, Oct 29, 2026)

- Email: `mmcclung1124@gmail.com`  
- LinkedIn: https://www.linkedin.com/in/mrmcclung  
- Phone: keep on the résumé page / PDF only (as provided)  
- Site purpose: job search  

### Updating the résumé

1. Re-save / export the PDF from the source document so the LinkedIn header text stays clean (`linkedin.com/in/mrmcclung`, not `/en/`).  
2. Replace `assets/resume/Michael-McClung-Resume-2025.pdf` with that file (keep the path/name unless you update every link + sitemap + quality check).  
3. Mirror facts into `main/resume/index.html` and the homepage experience/skills sections.  
4. Keep Contact / Download Resume / LinkedIn CTAs on every page.  
5. Spot-check PDF: size ≫ 60 bytes, starts with `%PDF`, contains `%%EOF`.

### Adding a project card

1. Add a card on `index.html` (projects section) and/or `main/projects/index.html`.  
2. Use HTTPS links and `rel="noopener noreferrer"` on `target="_blank"`.  
3. Do not invent employers, metrics, or features.  
4. Note: **RollWithDFW** is a project card linking to https://rollwithdfw.com; it is **not** listed on the HTML résumé (pending Mac’s review whether it should appear there).

### Re-running link checks and Lighthouse

```bash
python3 scripts/build_static.py
cd _site && python3 -m http.server 8080
# curl internal paths; open PDF URL
# Lighthouse (Chrome DevTools or CLI) against the local home page — record in TEST-RESULTS.md
```

After merge, re-check production URLs and record scores separately. LinkedIn often cannot be bot-verified (exclude or treat as inconclusive). Quality workflow already excludes `linkedin.com` from lychee hard-fail.

---

## Known limitations

1. **LinkedIn** is not reliably bot-verifiable (anti-bot / 999 / captcha). Human browser check required.  
2. **RollWithDFW** appears as a project card (separate site) but is **not** on the résumé — pending Mac’s review.  
3. **Lighthouse** scores on record cover the **home page** only (local serve), not every route.  
4. Production post-merge checks remain pending until `renovation/portfolio-2026` is merged and Pages redeploys.  
5. No Gemfile pins local Jekyll to CI; rely on `build_static.py` or Pages action Ruby set.  
6. Anonymous GitHub Pages settings API remains unavailable; deploy is inferred from Actions + live host.  

See `TEST-RESULTS.md` for measured vs not-yet-measured rows.
