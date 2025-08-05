from datetime import datetime, timedelta

def generate_items():
    now = datetime.utcnow()
    items = []

    # Good events (3)
    for i in range(3):
        ts = now - timedelta(seconds=i * 30)
        pub_date = ts.strftime('%a, %d %b %Y %H:%M:%S +0000')
        iso = ts.isoformat() + "Z"
        guid = f"good-{int(ts.timestamp())}"
        items.append(f"""  <item>
    <title>Good Event {i + 1}</title>
    <description>Updated at {iso}</description>
    <pubDate>{pub_date}</pubDate>
    <guid>{guid}</guid>
  </item>""")

    # Events with invalid pubDate (3)
    for i in range(3):
        ts = now - timedelta(seconds=90 + i * 30)
        iso = ts.isoformat() + "Z"
        guid = f"invalid-pubdate-{int(ts.timestamp())}"
        items.append(f"""  <item>
    <title>Invalid PubDate Event {i + 1}</title>
    <description>Updated at {iso}</description>
    <pubDate>LALALALA</pubDate>
    <guid>{guid}</guid>
  </item>""")

    # Events with missing pubDate (3)
    for i in range(3):
        ts = now - timedelta(seconds=180 + i * 30)
        iso = ts.isoformat() + "Z"
        guid = f"no-pubdate-{int(ts.timestamp())}"
        items.append(f"""  <item>
    <title>No PubDate Event {i + 1}</title>
    <description>Updated at {iso}</description>
    <guid>{guid}</guid>
  </item>""")

    return "\n".join(items)

def generate_rss():
    return f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>My Test Feed</title>
  <link>https://eladsapirblink.github.io/RssFeed/feed.xml</link>
  <description>RSS feed with mixed valid and invalid events.</description>
{generate_items()}
</channel>
</rss>"""

if __name__ == "__main__":
    with open("feed.xml", "w") as f:
        f.write(generate_rss())
