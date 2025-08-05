import os
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

FEED_FILE = "feed.xml"
MAX_ITEMS = 50

def read_existing_items():
    items = []
    if os.path.exists("items.txt"):
        with open("items.txt", "r") as f:
            for line in f:
                title, timestamp = line.strip().split("|")
                items.append({
                    "title": title,
                    "pubDate": timestamp,
                    "description": f"This is {title} generated at {timestamp}",
                    "link": f"https://your-username.github.io/test-rss-feed/{title.replace(' ', '_')}"
                })
    return items

def save_items(items):
    with open("items.txt", "w") as f:
        for item in items:
            f.write(f"{item['title']}|{item['pubDate']}\n")

def generate_feed(items):
    rss = Element('rss', version='2.0')
    channel = SubElement(rss, 'channel')
    SubElement(channel, 'title').text = "Test Feed"
    SubElement(channel, 'link').text = "https://your-username.github.io/test-rss-feed/feed.xml"
    SubElement(channel, 'description').text = "Auto-generated test news feed"

    for item in items:
        it = SubElement(channel, 'item')
        SubElement(it, 'title').text = item['title']
        SubElement(it, 'link').text = item['link']
        SubElement(it, 'pubDate').text = item['pubDate']
        SubElement(it, 'description').text = item['description']

    xml_str = parseString(tostring(rss)).toprettyxml(indent="  ")
    with open(FEED_FILE, "w") as f:
        f.write(xml_str)

def main():
    items = read_existing_items()
    now = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')
    new_item = {
        "title": f"Test News {len(items)+1}",
        "pubDate": now,
        "description": f"This is test news item generated at {now}",
        "link": f"https://EladSapirBlink.github.io/test-rss-feed/test-news-{len(items)+1}"
    }
    items.insert(0, new_item)
    items = items[:MAX_ITEMS]
    save_items(items)
    generate_feed(items)

if __name__ == "__main__":
    main()
