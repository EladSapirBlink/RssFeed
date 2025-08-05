from datetime import datetime

rss_items = f"""
<item>
  <title>Feed Update</title>
  <description>Updated at {datetime.utcnow().isoformat()}Z</description>
  <pubDate>{datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')}</pubDate>
  <guid>update-{datetime.utcnow().timestamp()}</guid>
</item>
"""

rss_feed = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>My Simple Feed</title>
  <link>https://eladsapirblink.github.io/RssFeed/feed.xml</link>
  <description>A simple RSS feed that updates every minute.</description>
  {rss_items}
</channel>
</rss>"""

with open("feed.xml", "w") as f:
    f.write(rss_feed)
