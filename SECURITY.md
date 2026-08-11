# Security Policy

This repository hosts Michael McClung's public portfolio website through GitHub Pages.

## Reporting a security issue

Please do not open a public issue for a suspected vulnerability that could expose private information or enable abuse. Report security concerns privately by emailing `michael.mcclung08@gmail.com` with a description of the issue and the affected page or file.

## Site security practices

- The site is static and does not process passwords, payments, or other sensitive user data.
- External links opened in a new tab use `rel="noopener"` to prevent tabnabbing.
- A restrictive Content Security Policy limits which origins may load scripts, styles, fonts, images, frames, and connections.
- Mixed-content requests are upgraded to HTTPS where supported.
- Changes should be reviewed through pull requests before reaching the default branch.
- GitHub Pages HTTPS should remain enforced in repository Pages settings.

## Supported version

Only the current version deployed from the repository's default branch is supported.