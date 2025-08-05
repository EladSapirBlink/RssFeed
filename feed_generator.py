from datetime import datetime, timedelta

def generate_items():
    now = datetime.utcnow()
    items = []
    for i in range(10):
        ts = now - timedelta(seconds=i * 30)
        pub_date = ts.strftime('%a, %d %b %Y %H:%M:%S +0000')
        iso = ts.isoformat() + "Z"
        guid = f"update-{int(ts.timestamp())}"
        items.append(f"""  <item>
    <title>Feed Update {i + 1}</title>
    <description>Updated at {iso}</description>
    <pubDate>{pub_date}</pubDate>
    <guid>{guid}</guid>
  </item>""")
    return "\n".join(items)

def generate_rss():
    return f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>My Simple Feed</title>
  <link>https://eladsapirblink.github.io/RssFeed/feed.xml</link>
  <description>RSS feed that updates every minute.</description>
{generate_items()}
</channel>
</rss>"""

if __name__ == "__main__":
    with open("feed.xml", "w") as f:
        f.write(generate_rss())
