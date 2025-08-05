import json
from datetime import datetime
import os

ITEMS_FILE = "feed_items.json"
MAX_ITEMS = 50

def load_items():
    if os.path.exists(ITEMS_FILE):
        with open(ITEMS_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_items(items):
    with open(ITEMS_FILE, "w") as f:
        json.dump(items, f, indent=2)

def create_item():
    now = datetime.utcnow()
    iso = now.isoformat() + "Z"
    pub_date = now.strftime('%a, %d %b %Y %H:%M:%S +0000')
    guid = f"update-{int(now.timestamp())}"
    return {
        "title": "Feed Update",
        "description": f"Updated at {iso}",
        "pubDate": pub_date,
        "guid": guid
    }

def generate_rss(items):
    rss_items_str = ""
    for item in items:
        rss_items_str += f"""
  <item>
    <title>{item['title']}</title>
    <description>{item['description']}</description>
    <pubDate>{item['pubDate']}</pubDate>
    <guid>{item['guid']}</guid>
  </item>
"""
    rss_feed = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>My Simple Feed</title>
  <link>https://eladsapirblink.github.io/RssFeed/feed.xml</link>
  <description>A simple RSS feed that updates every minute with the last 50 updates.</description>
  {rss_items_str}
</channel>
</rss>"""
    return rss_feed

def main():
    items = load_items()
    new_item = create_item()
    items.append(new_item)

    # Sort by pubDate descending (most recent first)
    items.sort(key=lambda x: x['pubDate'], reverse=True)

    # Keep only last MAX_ITEMS
    items = items[:MAX_ITEMS]

    save_items(items)

    rss_feed = generate_rss(items)
    with open("feed.xml", "w") as f:
        f.write(rss_feed)

if __name__ == "__main__":
    main()
