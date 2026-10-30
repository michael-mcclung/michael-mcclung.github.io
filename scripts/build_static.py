#!/usr/bin/env python3
"""Minimal Jekyll-like build for local preview: expands {% include %} and filters."""
from __future__ import annotations
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"
SITE_URL = "https://michael-mcclung.github.io"
INCLUDES = ROOT / "_includes"

INCLUDE_RE = re.compile(r"\{%\s*include\s+([^\s%]+)\s*%\}")
REL_RE = re.compile(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}")
ABS_RE = re.compile(r"\{\{\s*'([^']+)'\s*\|\s*absolute_url\s*\}\}")
PAGE_URL_ABS = re.compile(r"\{\{\s*page\.url\s*\|\s*absolute_url\s*\}\}")
PAGE_TITLE = re.compile(r"\{%\s*if\s+page\.title\s*%\}\{\{\s*page\.title\s*\}\}\s*\|\s*\{%\s*endif\s*%\}")
FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)


def parse_front_matter(text: str):
    m = FRONT_MATTER.match(text)
    meta = {}
    body = text
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")
        body = text[m.end():]
    return meta, body


def relative_url(path: str) -> str:
    return path if path.startswith("/") else "/" + path


def absolute_url(path: str) -> str:
    return SITE_URL.rstrip("/") + relative_url(path)


def render(text: str, page_url: str = "/", page_title: str = "") -> str:
    def incl(m):
        name = m.group(1).strip()
        inc_path = INCLUDES / name
        if not inc_path.exists():
            raise FileNotFoundError(inc_path)
        return render(inc_path.read_text(), page_url=page_url, page_title=page_title)

    text = INCLUDE_RE.sub(incl, text)
    text = REL_RE.sub(lambda m: relative_url(m.group(1)), text)
    text = ABS_RE.sub(lambda m: absolute_url(m.group(1)), text)
    text = PAGE_URL_ABS.sub(absolute_url(page_url), text)
    text = PAGE_TITLE.sub((page_title + " | ") if page_title else "", text)
    text = re.sub(r"\{\%.*?\%\}", "", text)
    text = re.sub(r"\{\{.*?\}\}", "", text)
    return text


def copy_static():
    for name in ["assets", "robots.txt", "sitemap.xml", "SECURITY.md"]:
        src = ROOT / name
        dst = OUT / name
        if src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        elif src.is_file():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


def build_page(src: Path, dest: Path, page_url: str):
    meta, body = parse_front_matter(src.read_text())
    html = render(body, page_url=page_url, page_title=meta.get("title", ""))
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    copy_static()
    pages = [
        (ROOT / "index.html", OUT / "index.html", "/"),
        (ROOT / "main/journey/index.html", OUT / "main/journey/index.html", "/main/journey/"),
        (ROOT / "main/projects/index.html", OUT / "main/projects/index.html", "/main/projects/"),
        (ROOT / "main/resume/index.html", OUT / "main/resume/index.html", "/main/resume/"),
    ]
    for src, dest, url in pages:
        build_page(src, dest, url)
        print("built", dest.relative_to(OUT))
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
