#!/usr/bin/env python3
"""Static SEO, structured-data, sitemap, and internal-link checks."""
from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://budzetplus.rs"
SKIP_FILES = {ROOT / "404.html"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_parts: list[str] = []
        self.in_title = False
        self.h1_count = 0
        self.description: str | None = None
        self.canonical: str | None = None
        self.links: list[str] = []
        self.json_ld: list[str] = []
        self._json_parts: list[str] | None = None

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrs_list)
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "meta" and attrs.get("name") == "description":
            self.description = attrs.get("content")
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        elif tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"] or "")
        elif tag == "script" and attrs.get("type") == "application/ld+json":
            self._json_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self._json_parts is not None:
            self.json_ld.append("".join(self._json_parts))
            self._json_parts = None

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self._json_parts is not None:
            self._json_parts.append(data)

    @property
    def title(self) -> str:
        return "".join(self.title_parts).strip()


def expected_url(path: Path) -> str:
    relative = path.relative_to(ROOT)
    if relative == Path("index.html"):
        return f"{BASE}/"
    return f"{BASE}/{relative.parent.as_posix()}/"


def internal_target(page: Path, href: str) -> Path | None:
    parsed = urlparse(href)
    if parsed.scheme in {"mailto", "tel", "viber"} or href.startswith("#"):
        return None
    if parsed.netloc and parsed.netloc != "budzetplus.rs":
        return None
    raw_path = unquote(parsed.path)
    if parsed.netloc:
        target = ROOT / raw_path.lstrip("/")
    else:
        target = page.parent / raw_path
    target = target.resolve()
    if target.is_dir() or raw_path.endswith("/"):
        target /= "index.html"
    return target


def main() -> int:
    errors: list[str] = []
    titles: dict[str, Path] = {}
    pages = sorted(p for p in ROOT.rglob("*.html") if p not in SKIP_FILES)
    canonical_urls: set[str] = set()

    for page in pages:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        rel = page.relative_to(ROOT)
        if not parser.title:
            errors.append(f"{rel}: missing title")
        elif parser.title in titles:
            errors.append(f"{rel}: duplicate title also used by {titles[parser.title].relative_to(ROOT)}")
        else:
            titles[parser.title] = page
        if not parser.description:
            errors.append(f"{rel}: missing meta description")
        if parser.h1_count != 1:
            errors.append(f"{rel}: expected exactly one h1, found {parser.h1_count}")
        expected = expected_url(page)
        if parser.canonical != expected:
            errors.append(f"{rel}: canonical is {parser.canonical!r}, expected {expected!r}")
        canonical_urls.add(expected)
        for block in parser.json_ld:
            try:
                json.loads(block)
            except json.JSONDecodeError as exc:
                errors.append(f"{rel}: invalid JSON-LD: {exc}")
        for href in parser.links:
            target = internal_target(page, href)
            if target is not None and ROOT not in target.parents and target != ROOT:
                errors.append(f"{rel}: internal link escapes site root: {href}")
            elif target is not None and not target.exists():
                errors.append(f"{rel}: broken internal link {href} -> {target.relative_to(ROOT)}")

    tree = ET.parse(ROOT / "sitemap.xml")
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = {node.text for node in tree.findall("sm:url/sm:loc", namespace) if node.text}
    missing_from_sitemap = canonical_urls - sitemap_urls
    extra_in_sitemap = sitemap_urls - canonical_urls
    for url in sorted(missing_from_sitemap):
        errors.append(f"sitemap: missing {url}")
    for url in sorted(extra_in_sitemap):
        errors.append(f"sitemap: URL has no matching HTML page: {url}")

    if errors:
        print("SEO checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"SEO checks passed for {len(pages)} pages and {len(sitemap_urls)} sitemap URLs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
