# Michael McClung — Personal Portfolio

Public portfolio for **Michael McClung** (Mac), Full Stack Software Engineer.

- **Live site (production):** https://michael-mcclung.github.io  
- **Repository:** https://github.com/michael-mcclung/michael-mcclung.github.io  
- **Default branch:** `master`  
- **Renovation branch (local):** `renovation/portfolio-2026`  
- **Recovery tag:** `pre-renovation-2026-10-29` → `fda53c8546c14e156bf7a67419198bffd3aa1353`

Job-hunt focused site for recruiters and hiring managers: clear Contact / Download Resume / LinkedIn CTAs, HTML résumé + PDF, experience, projects, and skills.

## Tech stack

| Layer | Choice |
|-------|--------|
| Markup | Static HTML + Jekyll Liquid includes (`{% include %}`) |
| Config | `_config.yml` (`theme: null`, `url` set for Pages) |
| Styles | Single consolidated `assets/css/site.css` (no Bootstrap) |
| Fonts | Google Fonts — Inter (free) |
| Scripts | `assets/js/site.js` (mobile nav, reveal, year) |
| Build / deploy | GitHub Actions → `actions/jekyll-build-pages` → `deploy-pages` |
| Hosting | GitHub Pages (`*.github.io`), no custom domain |
| Cost | $0 — mailto contact, free fonts/icons, no paid analytics/forms |

There is **no Gemfile**; CI uses GitHub’s Jekyll Pages build action. A small Python helper `scripts/build_static.py` expands includes for local preview without Ruby.

## Local setup

### Prerequisites

- Git  
- Python 3 (for `scripts/build_static.py` local preview)  
- Optional: Ruby/Jekyll matching GitHub Pages for a faithful CI-like build  

### Clone

```bash
git clone https://github.com/michael-mcclung/michael-mcclung.github.io.git
cd michael-mcclung.github.io
git checkout renovation/portfolio-2026   # when working on this renovation
```

### Preferred local preview (no Ruby)

```bash
python3 scripts/build_static.py
cd _site && python3 -m http.server 8080
# open http://127.0.0.1:8080
```

### Jekyll (CI-faithful)

```bash
jekyll serve
# or after a Gemfile is added: bundle exec jekyll serve
```

## Site structure

```
index.html                 Home (hero, about, experience, projects, skills, resume CTA, contact)
main/journey/index.html    Experience
main/projects/index.html   Projects
main/resume/index.html     HTML résumé (print-friendly)
assets/resume/Michael-McClung-Resume-2025.pdf
assets/css/site.css
assets/js/site.js
assets/img/                portrait + favicon
_includes/                 head, navbar, footer
robots.txt / sitemap.xml
.github/workflows/         deploy + security + quality checks
SECURITY.md
```

## Deployment (GitHub Pages)

1. Merge or push to `master` (or run **Build and deploy Jekyll site to GitHub Pages** via `workflow_dispatch`).  
2. `.github/workflows/deploy.yml` builds with `actions/jekyll-build-pages@v1` and deploys with `actions/deploy-pages@v4`.  
3. Site is served at https://michael-mcclung.github.io.

**Do not change Pages deployment settings** as part of routine content work. PR checks run via `site-security-check.yml` and `site-quality-check.yml` (html-proofer / lychee + security basics).

## Rollback

**Never force-push `master` for routine rollbacks.**

1. Prefer reverting the bad PR/merge with a forward revert PR into `master`.  
2. Or restore content from the recovery tag / SHA and open a normal PR:

```bash
git checkout -b rollback/pre-renovation-2026-10-29
git checkout pre-renovation-2026-10-29 -- .
git commit -m "Rollback site content to pre-renovation-2026-10-29 (fda53c8)"
# push branch + open PR → merge to master → wait for Pages deploy
```

Recovery tag: `pre-renovation-2026-10-29` = `fda53c8546c14e156bf7a67419198bffd3aa1353`  
(“Fix resume page and render resume directly”, 2026-08-11).

Confirm https://michael-mcclung.github.io after deploy finishes.

## Content rules

- Public email: `mmcclung1124@gmail.com`  
- LinkedIn (site): https://www.linkedin.com/in/mrmcclung  
- Phone appears on the résumé page/PDF only as provided  
- Do not invent employers, dates, degrees, metrics, or project features  
- RollWithDFW is a **separate site** (https://rollwithdfw.com); linked as its own project card  

### Updating the résumé

1. Replace `assets/resume/Michael-McClung-Resume-2025.pdf` with a valid current PDF.  
2. Mirror facts into `main/resume/index.html` and homepage experience/skills sections.  
3. Keep Contact / Download Resume / LinkedIn CTAs on every page.

## Security

- No `http://` asset or link URLs (security workflow fails on them).  
- CSP lives in `_includes/head.html`.  
- Report vulnerabilities privately per `SECURITY.md`.
