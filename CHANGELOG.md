# Changelog

All notable changes to [michael-mcclung.github.io](https://github.com/michael-mcclung/michael-mcclung.github.io) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) where version tags are used. The portfolio renovation is merged to `master` (PR #3, `1a36f4f`, Oct 29, 2026) and live on GitHub Pages. Rollback tag `pre-renovation-2026-10-29` points to `fda53c8`.

## [2026-10-30] — docs sync

- Docs only (no site files). PR #3 (portfolio renovation) merged as `1a36f4f` on Oct 29, 2026 and is live at https://michael-mcclung.github.io/ via GitHub Pages. Rollback tag `pre-renovation-2026-10-29` points to `fda53c8`.
- Live production Lighthouse (home page, measured Oct 29, 2026): mobile Performance 93, Accessibility 100, Best Practices 100, SEO 100; desktop 99/100/100/100.
- PR #4 (RollWithDFW card points to `archive/sushi-app`) is merged and live. rollwithdfw.com serves the RollWithDFW tenant site (rollwithdfw repo PR #1, merged as `002fd40`, deployed on Netlify on Oct 30, 2026). The sushi app is archived as tag `sushi-app-archive-2026-10-30` and branch `archive/sushi-app` at `75a7a5a`.

## [2026-10-29] — renovation/portfolio-2026 (merged as PR #3, `1a36f4f`)

Verified from local branch tip `c25c2f7f3a730e9c9647788c1bfab7e1ff277733` (`git diff master...renovation/portfolio-2026` at documentation time). Commits: `d61ab91` (layout + resume), `c25c2f7` (docs/SEO/CI helper).

- `386bfbd`: About section now shows resume results near the top (1,000+ developer hours, 64% fewer chargebacks, 2× revenue, 20% lower time and fuel costs), and the RollWithDFW cards link to the source repo on GitHub.

### Mac’s confirmed decisions (Oct 29, 2026, America/Chicago)

- Public email: **`mmcclung1124@gmail.com`**
- Phone **stays on the resume page** (and PDF)
- **2025 resume is current**; the broken 60-byte PDF was replaced with Mac’s working copy; LinkedIn header fixed to **`/in/`**
- LinkedIn link fixed to **`linkedin.com/in/mrmcclung`** (site uses `https://www.linkedin.com/in/mrmcclung`)
- Both concurrent job date ranges are **correct** (Property Manager 2025–Present concurrent with Affordable Air Lead Dispatch Manager 2025–2026)
- Site purpose: **Mac’s job search**
- Headline: **Michael McClung, Full Stack Software Engineer**, with subline **“I build software that fixes real business operations”** (implemented as H1 + role line + lead)

### Added

- Recovery tag **`pre-renovation-2026-10-29`** at `fda53c8546c14e156bf7a67419198bffd3aa1353` (present on local renovation working copy)
- Design system: `assets/css/site.css`; mobile nav; `prefers-reduced-motion` handling; skip link
- Homepage sections: hero, About, Experience, Projects, Skills, Resume CTA, Contact
- Valid résumé PDF: `assets/resume/Michael-McClung-Resume-2025.pdf` (~96 KB)
- Assets: `assets/img/portrait.jpg`, `assets/img/favicon.svg`, `assets/js/site.js`
- SEO: Open Graph / Twitter meta, canonical URLs, `robots.txt`, `sitemap.xml`
- `.gitignore` (includes `_site/`, `.DS_Store`, Jekyll/vendor noise)
- GitHub Actions **`site-quality-check.yml`** (Jekyll build, html-proofer internal links, lychee external with LinkedIn/fonts excluded, security basics + PDF file check) on PRs/pushes to `master`
- Local preview helper `scripts/build_static.py`
- In-repo `README.md` and `CHANGELOG.md` on the renovation branch

### Changed

- Recruiter / job-search positioning and CTAs (Contact, Download Resume, LinkedIn) on every page
- Public contact email standardized to `mmcclung1124@gmail.com`
- LinkedIn site links use `https://www.linkedin.com/in/mrmcclung`
- Concurrent ops roles called out in experience copy
- Removed Bootstrap CDN; CSP tightened (`script-src 'self'` only among CDNs fonts remain for CSS)
- `_config.yml` gains `title`, `description`, `url`, `baseurl`
- Footer year dynamic via `site.js`; nested `<head>` include fixed (include no longer wraps its own `<head>`)
- Portrait moved from repo-root `indexSelfie.jpg` to `assets/img/portrait.jpg`
- RollWithDFW project card pointed to https://rollwithdfw.com (separate site) in this renovation. The live card points at `archive/sushi-app` (see 2026-10-30).

### Removed

- Broken / truncated `main/resume/2025 Resume .pdf` (60-byte invalid file)
- Unreferenced `main/projects/Final Video V2.mp4` (~25 MB)
- Fragmented / unused CSS: `style.css`, `modern.css`, `portfolio.css`, `showcase-home.css`, `mainStyles.css`
- Tracked `.DS_Store` files

### Fixed

- Resume download serves a real PDF with LinkedIn path `/in/mrmcclung`
- Incorrect résumé LinkedIn `/en/` path removed from HTML
- Resume HTML aligned to the current 2025 PDF as source of truth (per renovation commit)

### Security

- CSP updated for self-hosted JS (no jsDelivr scripts); `upgrade-insecure-requests` retained
- Quality workflow asserts PDF path exists and repeats insecure-`http://` scan

## [Production baseline] — 2026-08-11

Served from `master` until PR #3 merged (`1a36f4f`, Oct 29, 2026). This SHA remains the rollback target.

- **SHA:** `fda53c8546c14e156bf7a67419198bffd3aa1353`
- **Tag:** `pre-renovation-2026-10-29`
- **Commit time:** Aug 11, 2026, 1:12:23 PM CT
- **Message:** Fix resume page and render resume directly
- **URL:** https://michael-mcclung.github.io (this baseline SHA is the rollback target; the URL serves the merged renovation)
- **Rollback:** Revert merge PR or restore from tag via normal commit/PR — **never force-push `master`**
