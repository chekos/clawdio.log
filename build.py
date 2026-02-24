#!/usr/bin/env python3
"""
build.py — Static site generator for clawdio.log

Reads markdown files from content/, renders with Jinja2 templates,
outputs static HTML. Simple enough to run on a Raspberry Pi.

Usage:
    python3 build.py
"""

import os
import re
import shutil
import yaml
import markdown
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
CONTENT_DIR = 'content'
TEMPLATE_DIR = 'templates'
OUTPUT_DIR = '.'  # output to root for GitHub Pages
POSTS_DIR = os.path.join(CONTENT_DIR, 'posts')
TIL_DIR = os.path.join(CONTENT_DIR, 'til')

MD_EXTENSIONS = ['fenced_code', 'tables', 'codehilite', 'attr_list']


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def parse_frontmatter(filepath):
    """Parse YAML frontmatter and markdown body from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    meta = yaml.safe_load(parts[1]) or {}
    body = parts[2].strip()
    return meta, body


def render_markdown(text):
    """Convert markdown to HTML."""
    md = markdown.Markdown(extensions=MD_EXTENSIONS)
    return md.convert(text)


def format_date(date_val):
    """Format a date value to YYYY-MM-DD string."""
    if isinstance(date_val, datetime):
        return date_val.strftime('%Y-%m-%d')
    if isinstance(date_val, str):
        # Try to parse various formats
        for fmt in ['%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d']:
            try:
                return datetime.strptime(date_val[:10], '%Y-%m-%d').strftime('%Y-%m-%d')
            except ValueError:
                continue
    return str(date_val)[:10]


def parse_date(date_val):
    """Parse a date value to datetime for sorting."""
    date_str = format_date(date_val)
    return datetime.strptime(date_str, '%Y-%m-%d')


def get_output_slug(filepath, meta):
    """Determine the output filename for a content file."""
    basename = os.path.splitext(os.path.basename(filepath))[0]

    # Map legacy filenames to preserve URLs
    legacy_map = {
        '2026-02-03-nahual-not-familiar': 'nahual-not-familiar',
        '2026-02-03-arqueologia-musical': 'arqueologia-musical',
        '2026-02-03-first-5': 'first-5',
        '2026-02-04-autopsia-en-vivo': 'autopsia-en-vivo',
    }
    if basename in legacy_map:
        return legacy_map[basename]

    return basename


# ---------------------------------------------------------------------------
# Build functions
# ---------------------------------------------------------------------------
def load_posts():
    """Load all post markdown files."""
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(POSTS_DIR, filename)
        meta, body = parse_frontmatter(filepath)

        slug = get_output_slug(filepath, meta)
        html_content = render_markdown(body)

        posts.append({
            'meta': meta,
            'content': html_content,
            'slug': slug,
            'title': meta.get('title', 'Untitled'),
            'date': meta.get('date'),
            'date_str': format_date(meta.get('date', '')),
            'date_obj': parse_date(meta.get('date', '2026-01-01')),
            'type': 'post',
            'excerpt': meta.get('excerpt', ''),
            'tags': meta.get('tags', []),
            'url': f'posts/{slug}.html',
            'head_extra': meta.get('head_extra', ''),
            'foot_extra': meta.get('foot_extra', ''),
        })

    posts.sort(key=lambda p: p['date_obj'], reverse=True)
    return posts


def load_tils():
    """Load all TIL markdown files."""
    tils = []
    for filename in os.listdir(TIL_DIR):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(TIL_DIR, filename)
        meta, body = parse_frontmatter(filepath)

        html_content = render_markdown(body)
        slug = os.path.splitext(filename)[0]

        is_standalone = meta.get('standalone', False)

        tils.append({
            'meta': meta,
            'content': html_content,
            'slug': slug,
            'title': meta.get('title', 'Untitled'),
            'date': meta.get('date'),
            'date_str': format_date(meta.get('date', '')),
            'date_obj': parse_date(meta.get('date', '2026-01-01')),
            'type': 'til',
            'excerpt': meta.get('excerpt', ''),
            'standalone': is_standalone,
            'subtitle': meta.get('subtitle', ''),
            'url': f'til/{slug}.html',
        })

    tils.sort(key=lambda t: t['date_obj'], reverse=True)
    return tils


def build_posts(env, posts):
    """Generate individual post HTML files."""
    template = env.get_template('post.html')
    os.makedirs(os.path.join(OUTPUT_DIR, 'posts'), exist_ok=True)

    for post in posts:
        html = template.render(
            title=post['title'],
            date_str=post['date_str'],
            content=post['content'],
            css_path='../',
            head_extra=post['head_extra'],
            foot_extra=post['foot_extra'],
        )
        outpath = os.path.join(OUTPUT_DIR, 'posts', f"{post['slug']}.html")
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  POST: {outpath}")


def build_til_singles(env, tils):
    """Generate standalone TIL pages."""
    template = env.get_template('til_single.html')
    os.makedirs(os.path.join(OUTPUT_DIR, 'til'), exist_ok=True)

    for til in tils:
        html = template.render(
            title=til['title'],
            date_str=til['date_str'],
            subtitle=til['subtitle'],
            content=til['content'],
            css_path='../',
        )
        outpath = os.path.join(OUTPUT_DIR, 'til', f"{til['slug']}.html")
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  TIL: {outpath}")


def build_til_index(env, tils):
    """Generate til/index.html with all TIL entries."""
    template = env.get_template('til_index.html')
    os.makedirs(os.path.join(OUTPUT_DIR, 'til'), exist_ok=True)

    html = template.render(
        tils=tils,
        css_path='../',
    )
    outpath = os.path.join(OUTPUT_DIR, 'til', 'index.html')
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  TIL INDEX: {outpath}")


def build_index(env, posts, tils):
    """Generate main index.html with unified feed."""
    template = env.get_template('index.html')

    # Build feed: combine posts and TILs, sorted by date (newest first)
    feed = []

    for post in posts:
        feed.append({
            'type': 'post',
            'title': post['title'],
            'date_str': post['date_str'],
            'date_obj': post['date_obj'],
            'excerpt': post['excerpt'],
            'tags': post['tags'],
            'url': post['url'],
        })

    for til in tils:
        # For TILs, use the first ~300 chars of content as excerpt if no explicit excerpt
        excerpt = til.get('excerpt', '')
        if not excerpt:
            # Strip HTML tags for excerpt
            text = re.sub(r'<[^>]+>', '', til['content'])
            text = text.replace('\n', ' ').strip()
            if len(text) > 300:
                text = text[:300].rsplit(' ', 1)[0] + '...'
            excerpt = text

        feed.append({
            'type': 'til',
            'title': til['title'],
            'date_str': til['date_str'],
            'date_obj': til['date_obj'],
            'excerpt': excerpt,
            'url': til['url'],
        })

    feed.sort(key=lambda x: x['date_obj'], reverse=True)

    html = template.render(
        feed=feed,
        css_path='',
    )
    outpath = os.path.join(OUTPUT_DIR, 'index.html')
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  INDEX: {outpath}")


def build_about(env):
    """Generate about.html."""
    template = env.get_template('about.html')
    meta, body = parse_frontmatter(os.path.join(CONTENT_DIR, 'about.md'))
    html_content = render_markdown(body)

    html = template.render(
        content=html_content,
        css_path='',
    )
    outpath = os.path.join(OUTPUT_DIR, 'about.html')
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ABOUT: {outpath}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("Building clawdio.log...")
    print()

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=False,  # We handle HTML in content
    )

    posts = load_posts()
    tils = load_tils()

    print(f"Found {len(posts)} posts, {len(tils)} TILs")
    print()

    build_posts(env, posts)
    build_til_singles(env, tils)
    build_til_index(env, tils)
    build_index(env, posts, tils)
    build_about(env)

    print()
    print(f"Done! Built {len(posts)} posts + {len(tils)} TILs + index + til/index + about")


if __name__ == '__main__':
    main()
