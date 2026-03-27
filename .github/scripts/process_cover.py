import os, re
import requests
import datetime
from pathlib import Path

posts_dir = Path("_posts")

for md_file in posts_dir.glob("*.md"):
    content = md_file.read_text()
    
    # Parse frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        continue
    fm = fm_match.group(1)
    
    # Skip if already synced
    if re.search(r"^synced:\s*true", fm, re.MULTILINE):
        md_file.unlink()  # remove it, don't publish
        print(f"Skipping (already synced): {md_file.name}")
        continue
    
    # Extract date and slug for renaming
    date_match = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", fm, re.MULTILINE)
    slug_match = re.search(r"^slug:\s*(.+)", fm, re.MULTILINE)
    
    if date_match and slug_match:
        date = date_match.group(1)
        slug = slug_match.group(1).strip()
        new_name = posts_dir / f"{date}-{slug}.md"
        md_file.rename(new_name)
        print(f"Renamed: {md_file.name} → {new_name.name}")

    # Set flag ToSync to false 
    id_match = re.search(r"^id:\s*(.+)", fm, re.MULTILINE)
    page_id = id_match.group(1).strip() if id_match else None

    if page_id:
        requests.patch(
            f"https://api.notion.com/v1/pages/{page_id}",
            headers={
                "Authorization": f"Bearer {os.environ['NOTION_API_KEY']}",
                "Notion-Version": "2022-06-28",
                "Content-Type": "application/json",
            },
            json={"properties": {"ToSync": {"checkbox": False}}}
    )
    print(f"Marked ToSync=false in Notion for page: {page_id}")
