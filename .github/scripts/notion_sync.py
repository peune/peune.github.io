import os
import re
import requests
from pathlib import Path
from datetime import datetime

NOTION_API_KEY = os.environ["NOTION_API_KEY"]
NOTION_DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

def query_pages():
    """Fetch only pages where ToSync = true"""
    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    payload = {
        "filter": {
            "property": "ToSync",
            "checkbox": {"equals": True}
        }
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["results"]

def get_page_markdown(page_id):
    """Use notion-to-md or just extract plain text blocks"""
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()["results"]

def blocks_to_markdown(blocks):
    """Basic block-to-markdown conversion"""
    lines = []
    for block in blocks:
        btype = block["type"]
        rich = block.get(btype, {}).get("rich_text", [])
        text = "".join([r["plain_text"] for r in rich])
        if btype == "heading_1":
            lines.append(f"# {text}")
        elif btype == "heading_2":
            lines.append(f"## {text}")
        elif btype == "heading_3":
            lines.append(f"### {text}")
        elif btype == "bulleted_list_item":
            lines.append(f"- {text}")
        elif btype == "numbered_list_item":
            lines.append(f"1. {text}")
        elif btype == "code":
            lang = block["code"].get("language", "")
            lines.append(f"```{lang}\n{text}\n```")
        elif btype == "paragraph":
            lines.append(text)
        else:
            if text:
                lines.append(text)
    return "\n\n".join(lines)

from PIL import Image, ImageOps

def get_cover(page, page_id, img_dir):
    """Download page cover and return relative path"""
    cover = page.get("cover")
    if not cover:
        return None
    
    # Cover can be external URL or Notion-hosted file
    if cover["type"] == "external":
        url = cover["external"]["url"]
    elif cover["type"] == "file":
        url = cover["file"]["url"]
    else:
        return None

    # Download the image
    img_dir.mkdir(parents=True, exist_ok=True)
    ext = url.split("?")[0].split(".")[-1]  # strip query params first
    img_path = img_dir / f"{page_id}_cover.{ext}"

    # Always download image just in case we want new version
    response = requests.get(url)
    response.raise_for_status()
    img_path.write_bytes(response.content)

    # Resize to fit Chirpy-Jekyll
    with Image.open(img_path) as img:
        # img = Image.open(img_path) 
    
        # Step 1: Resize width to 1200, keep aspect ratio
        target_width = 1200
        ratio = target_width / img.width
        new_height = int(img.height * ratio)
        resized = img.resize((target_width, new_height), Image.LANCZOS)
        print("new size ", resized.size)
        
        # Step 2: Pad vertically to 630px with white
        target_height = 630
        if new_height > target_height:
            # Fallback: crop center instead of padding
            padded = ImageOps.fit(resized, (target_width, target_height), Image.LANCZOS)
        else:
            pad_top = (target_height - new_height) // 2
            pad_bottom = target_height - new_height - pad_top
            padded = ImageOps.expand(resized, border=(0, pad_top, 0, pad_bottom), fill="white")

        print("new size with pad ", padded.size)

    # Overwrite the old image
    padded.save(img_path)
        
    print(f"Downloaded cover: {img_path}")
    
    return str(img_path)

def get_prop(props, name, prop_type):
    """Safely extract a property value"""
    prop = props.get(name, {})
    if prop_type == "title":
        return "".join([r["plain_text"] for r in prop.get("title", [])])
    elif prop_type == "rich_text":
        return "".join([r["plain_text"] for r in prop.get("rich_text", [])])
    elif prop_type == "date":
        d = prop.get("date")
        return d["start"][:10] if d else None
    elif prop_type == "status":
        s = prop.get("status")
        return s["name"] if s else None
    elif prop_type == "checkbox":
        return prop.get("checkbox", False)
    return None

def mark_synced(page_id):
    """Flip ToSync back to false in Notion"""
    requests.patch(
        f"https://api.notion.com/v1/pages/{page_id}",
        headers=HEADERS,
        json={"properties": {"ToSync": {"checkbox": False}}}
    )

# --- Main ---
posts_dir = Path("_posts")
posts_dir.mkdir(exist_ok=True)

img_dir = Path("img")
img_dir.mkdir(exist_ok=True)

pages = query_pages()
print(f"Found {len(pages)} pages to sync")

for page in pages:
    page_id = page["id"]
    props = page["properties"]

    slug = get_prop(props, "slug", "rich_text")
    date = get_prop(props, "Date", "date")
    title = get_prop(props, "Title", "title")

    if not slug or not date:
        print(f"Skipping {page_id}: missing slug or date")
        continue

    # Get cover
    cover_path = get_cover(page, page_id, img_dir)
    if cover_path:
        image_line = f"\nimage:\n  path: /{cover_path}\n  alt: {title}"
    else:
        image_line = ""
    
    # Build frontmatter
    frontmatter = f"""---
title: {title}
date: {date}
slug: {slug}{image_line}
---"""

    # Get content blocks
    blocks = get_page_markdown(page_id)
    body = blocks_to_markdown(blocks)

    # Write file
    safe_slug = slug.replace(' ', '-')
    filename = posts_dir / f"{date}-{safe_slug}.md"
    filename.write_text(f"{frontmatter}\n\n{body}\n")
    print(f"Written: {filename}")

    # Mark as synced in Notion
    mark_synced(page_id)
    print(f"Marked ToSync=false for: {page_id}")
