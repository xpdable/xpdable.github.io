#!/usr/bin/env python3
"""
Build script for XP's terminal-themed blog.

Reads markdown posts from content/posts/, renders them to HTML using the
terminal theme template, and updates the blog listing in index.html.
Also generates RSS feed (feed.xml) and sitemap (sitemap.xml).

Markdown format:
  ---
  title: Post Title
  date: 2023-07-11
  tags: [tag1, tag2]
  ---
  English content (original)...

  <!-- lang:zh -->
  Chinese content (AI translated)...

  <!-- lang:de -->
  German content (AI translated)...
"""

import re
import shutil
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.parse import quote

try:
    import markdown
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown"])
    import markdown

# --- Config ---
ROOT = Path(__file__).parent
CONTENT_DIR = ROOT / "content" / "posts"
TEMPLATE_PATH = ROOT / "templates" / "post.html"
OUTPUT_DIR = ROOT / "_site"
POSTS_OUTPUT = OUTPUT_DIR / "posts"

SITE_URL = "https://xpdable.github.io"
SITE_TITLE = "xpthink"
SITE_DESC = (
    "I used to believe code was everything. Chaos Engineering taught me "
    "better — thinking is what drives real success."
)
AUTHOR = "xp"

LANG_LABELS = {"en": "EN", "zh": "中文", "de": "DE"}
LANG_ORDER = ["en", "zh", "de"]

MD_EXTENSIONS = ["extra", "smarty", "sane_lists"]

SKIP_DIRS = {
    "_site", "content", "templates", ".git", ".github", "__pycache__", ".claude"
}
SKIP_FILES = {"build.py", "requirements.txt", ".gitignore"}


def parse_frontmatter(text):
    """Parse YAML-like frontmatter from markdown text."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}, text
    raw = match.group(1)
    body = text[match.end():]
    meta = {}
    for line in raw.strip().splitlines():
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            val = [v.strip().strip("'\"") for v in val[1:-1].split(",")]
        meta[key] = val
    return meta, body


def split_languages(body):
    """Split body by <!-- lang:xx --> markers. First section is always 'en'."""
    parts = re.split(r"<!--\s*lang:(\w+)\s*-->", body)
    langs = {"en": parts[0].strip()}
    for i in range(1, len(parts), 2):
        lang = parts[i].strip()
        content = parts[i + 1].strip() if i + 1 < len(parts) else ""
        langs[lang] = content
    return langs


def md_to_html(text):
    """Convert markdown to HTML."""
    return markdown.markdown(text, extensions=MD_EXTENSIONS)


def build_lang_buttons(langs):
    """Generate language switcher buttons HTML."""
    buttons = []
    for lang in LANG_ORDER:
        if lang not in langs:
            continue
        active = " active original" if lang == "en" else ""
        label = LANG_LABELS.get(lang, lang.upper())
        if lang == "en":
            badge = '<span class="lang-badge">original</span>'
        else:
            badge = '<span class="lang-badge ai">AI</span>'
        buttons.append(
            f'<button class="lang-btn{active}" data-lang="{lang}">'
            f"{label} {badge}</button>"
        )
    return "\n            ".join(buttons)


def build_lang_contents(langs):
    """Generate language content divs."""
    sections = []
    for lang in LANG_ORDER:
        if lang not in langs:
            continue
        active = " active" if lang == "en" else ""
        html_content = md_to_html(langs[lang])
        sections.append(
            f'<div class="lang-content{active}" data-lang="{lang}">\n'
            f'  <div class="post-content">\n{html_content}\n  </div>\n'
            f"</div>"
        )
    return "\n\n          ".join(sections)


def build_tags_html(tags):
    """Generate tag links for post meta line."""
    return " ".join(
        f'<a href="../index.html#blog" class="tag">{t}</a>' for t in tags
    )


def build_share_links(title, slug):
    """Generate share links HTML for a post."""
    url = quote(f"{SITE_URL}/posts/{slug}.html", safe="")
    encoded_title = quote(title)
    return (
        f'<div class="share-links">\n'
        f'  <span class="dim">$ share --via</span>\n'
        f'  <a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" '
        f'target="_blank" rel="noopener" class="share-btn">LinkedIn</a>\n'
        f'  <a href="https://twitter.com/intent/tweet?url={url}&text={encoded_title}" '
        f'target="_blank" rel="noopener" class="share-btn">X</a>\n'
        f'  <a href="mailto:?subject={encoded_title}&body={url}" '
        f'class="share-btn">Email</a>\n'
        f"</div>"
    )


def build_post(md_path, template):
    """Build a single post HTML from a markdown file."""
    text = md_path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    langs = split_languages(body)

    slug = md_path.stem
    title = meta.get("title", slug)
    date = str(meta.get("date", ""))
    tags = meta.get("tags", [])

    html = template
    html = html.replace("{{title}}", title)
    html = html.replace("{{date}}", date)
    html = html.replace("{{slug}}", slug)
    html = html.replace("{{tags_html}}", build_tags_html(tags))
    html = html.replace("{{lang_buttons}}", build_lang_buttons(langs))
    html = html.replace("{{lang_contents}}", build_lang_contents(langs))
    html = html.replace("{{share_links}}", build_share_links(title, slug))

    # English-only content for RSS (plain text summary)
    en_html = md_to_html(langs.get("en", ""))

    return html, {
        "slug": slug,
        "title": title,
        "date": date,
        "tags": tags,
        "en_html": en_html,
    }


def build_blog_listing(posts_meta):
    """Generate blog post rows and tag filter buttons for index.html."""
    all_tags = []
    for p in posts_meta:
        for t in p["tags"]:
            if t not in all_tags:
                all_tags.append(t)

    tag_buttons = ['<button class="tag-btn active" data-tag="all">all</button>']
    for tag in all_tags:
        tag_buttons.append(
            f'<button class="tag-btn" data-tag="{tag}">{tag}</button>'
        )
    tags_html = "\n              ".join(tag_buttons)

    posts_meta.sort(key=lambda p: p["date"], reverse=True)
    rows = []
    for p in posts_meta:
        tags_attr = ",".join(p["tags"])
        tag_spans = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
        rows.append(
            f'<a href="posts/{p["slug"]}.html" class="blog-post-row" '
            f'data-tags="{tags_attr}">\n'
            f'                <span class="post-date">{p["date"]}</span>\n'
            f'                <span class="post-title">{p["title"]}</span>\n'
            f'                <span class="post-tags">{tag_spans}</span>\n'
            f'                <span class="post-arrow">-&gt;</span>\n'
            f"              </a>"
        )
    rows_html = "\n              ".join(rows)

    return tags_html, rows_html


def update_index(index_html, posts_meta):
    """Replace blog listing markers in index.html with generated content."""
    tags_html, rows_html = build_blog_listing(posts_meta)

    index_html = re.sub(
        r"(<div class=\"blog-tags-filter\">)\s*.*?\s*(</div>)",
        rf"\1\n              {tags_html}\n            \2",
        index_html,
        flags=re.DOTALL,
    )

    index_html = re.sub(
        r"(<div class=\"blog-posts\">)\s*.*?\s*(</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</section>)",
        rf"\1\n              {rows_html}\n            \2",
        index_html,
        flags=re.DOTALL,
    )

    return index_html


def generate_rss(posts_meta):
    """Generate Atom feed XML."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entries = []
    for p in posts_meta:
        date = p["date"] + "T00:00:00Z" if len(p["date"]) == 10 else p["date"]
        post_url = f"{SITE_URL}/posts/{p['slug']}.html"
        content = escape(p.get("en_html", ""))
        entries.append(
            f"  <entry>\n"
            f"    <title>{escape(p['title'])}</title>\n"
            f"    <link href=\"{post_url}\" rel=\"alternate\" type=\"text/html\"/>\n"
            f"    <id>{post_url}</id>\n"
            f"    <published>{date}</published>\n"
            f"    <updated>{date}</updated>\n"
            f"    <author><name>{AUTHOR}</name></author>\n"
            f"    <content type=\"html\">{content}</content>\n"
            f"  </entry>"
        )
    entries_xml = "\n".join(entries)
    return (
        f'<?xml version="1.0" encoding="utf-8"?>\n'
        f'<feed xmlns="http://www.w3.org/2005/Atom">\n'
        f"  <title>{escape(SITE_TITLE)}</title>\n"
        f"  <subtitle>{escape(SITE_DESC)}</subtitle>\n"
        f"  <link href=\"{SITE_URL}/feed.xml\" rel=\"self\" type=\"application/atom+xml\"/>\n"
        f"  <link href=\"{SITE_URL}/\" rel=\"alternate\" type=\"text/html\"/>\n"
        f"  <id>{SITE_URL}/feed.xml</id>\n"
        f"  <updated>{now}</updated>\n"
        f"  <author><name>{AUTHOR}</name></author>\n"
        f"{entries_xml}\n"
        f"</feed>\n"
    )


def generate_sitemap(posts_meta):
    """Generate sitemap.xml."""
    urls = [
        f"  <url><loc>{SITE_URL}/</loc><priority>1.0</priority></url>",
        f"  <url><loc>{SITE_URL}/resume.html</loc><priority>0.8</priority></url>",
    ]
    for p in posts_meta:
        urls.append(
            f"  <url><loc>{SITE_URL}/posts/{p['slug']}.html</loc>"
            f"<lastmod>{p['date']}</lastmod><priority>0.7</priority></url>"
        )
    urls_xml = "\n".join(urls)
    return (
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls_xml}\n"
        f"</urlset>\n"
    )


def main():
    print("Building XP blog...")

    # Clean and create output dir
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    # Copy all static files to _site
    for item in ROOT.iterdir():
        if item.name in SKIP_DIRS or item.name in SKIP_FILES:
            continue
        dest = OUTPUT_DIR / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)

    # Copy .github separately (needed for Pages)
    github_dir = ROOT / ".github"
    if github_dir.exists():
        shutil.copytree(github_dir, OUTPUT_DIR / ".github")

    # Ensure posts output dir exists
    POSTS_OUTPUT.mkdir(parents=True, exist_ok=True)

    # Load template
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    # Build all posts
    posts_meta = []
    for md_file in sorted(CONTENT_DIR.glob("*.md")):
        print(f"  Building: {md_file.name}")
        html, meta = build_post(md_file, template)
        output_path = POSTS_OUTPUT / f"{meta['slug']}.html"
        output_path.write_text(html, encoding="utf-8")
        posts_meta.append(meta)

    # Sort by date descending
    posts_meta.sort(key=lambda p: p["date"], reverse=True)

    # Update index.html with blog listing
    index_html = (OUTPUT_DIR / "index.html").read_text(encoding="utf-8")
    index_html = update_index(index_html, posts_meta)
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

    # Generate RSS feed
    feed_xml = generate_rss(posts_meta)
    (OUTPUT_DIR / "feed.xml").write_text(feed_xml, encoding="utf-8")
    print("  Generated: feed.xml")

    # Generate sitemap
    sitemap_xml = generate_sitemap(posts_meta)
    (OUTPUT_DIR / "sitemap.xml").write_text(sitemap_xml, encoding="utf-8")
    print("  Generated: sitemap.xml")

    print(f"  Generated {len(posts_meta)} post(s)")
    print(f"  Output: {OUTPUT_DIR}/")
    print("Done!")


if __name__ == "__main__":
    main()
