# Changelog

All notable changes to [michael-mcclung.github.io](https://github.com/michael-mcclung/michael-mcclung.github.io) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased] — renovation/portfolio-2026 (2026-10-29)

### Added

- Recovery tag `pre-renovation-2026-10-29` at `fda53c8` (local).
- Consolidated design system in `assets/css/site.css` with mobile nav, `prefers-reduced-motion`, SEO / Open Graph / Twitter meta, SVG favicon.
- Sections on homepage: hero, About, Experience, Projects, Skills, Resume CTA, Contact.
- Working resume PDF at `assets/resume/Michael-McClung-Resume-2025.pdf`.
- `robots.txt`, `sitemap.xml`, `.gitignore`.
- GitHub Actions `site-quality-check.yml` (Jekyll build, html-proofer, lychee, security basics) on PRs/pushes to `master`.
- Local preview helper `scripts/build_static.py`.
- README documenting setup, deploy, and rollback to `pre-renovation-2026-10-29`.

### Changed

- Recruiter-focused positioning: H1 “Michael McClung”, role “Full Stack Software Engineer”, supporting line “I build software that fixes real business operations.”
- Public contact email standardized to `mmcclung1124@gmail.com`.
- LinkedIn site links use `https://www.linkedin.com/in/mrmcclung`.
- Property Manager (2025–Present) and Affordable Air Lead Dispatch Manager (2025–2026) shown as concurrent.
- Every page exposes Contact, Download Resume, and LinkedIn CTAs.
- Removed Bootstrap CDN dependency in favor of lightweight custom CSS/JS.
- Footer year is dynamic; copyright updated.

### Removed

- Broken / truncated `main/resume/2025 Resume .pdf` (60-byte invalid file).
- Unreferenced `main/projects/Final Video V2.mp4` (~25 MB).
- Unused `assets/css/mainStyles.css` and fragmented CSS (`style.css`, `modern.css`, `portfolio.css`, `showcase-home.css`) replaced by `site.css`.
- Tracked `.DS_Store` junk files.
- Duplicate root `indexSelfie.jpg` (portrait now `assets/img/portrait.jpg`).

### Fixed

- Nested `<head>` include markup.
- Resume content aligned to the current 2025 PDF (source of truth).
- PDF download serves a valid `%PDF` document (local check HTTP 200, ~96 KB).

## [Production baseline] — 2026-08-11

- **SHA:** `fda53c8546c14e156bf7a67419198bffd3aa1353`
- **Message:** Fix resume page and render resume directly
- **Tag:** `pre-renovation-2026-10-29`
- **Live URL:** https://michael-mcclung.github.io
