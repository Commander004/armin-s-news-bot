import feedparser
from config import RSS_FEEDS


def extract_image(entry):

    # 🖼️ حالت 1: media:content
    media = entry.get("media_content")
    if isinstance(media, list) and len(media) > 0:
        url = media[0].get("url")
        if url and url.startswith("http"):
            return url

    # 🖼️ حالت 2: media_thumbnail
    media_thumb = entry.get("media_thumbnail")
    if isinstance(media_thumb, list) and len(media_thumb) > 0:
        url = media_thumb[0].get("url")
        if url and url.startswith("http"):
            return url

    # 🖼️ حالت 3: enclosure
    enclosures = entry.get("enclosures")
    if isinstance(enclosures, list) and len(enclosures) > 0:
        url = enclosures[0].get("href")
        if url and url.startswith("http"):
            return url

    return None


def get_news():

    all_news = []

    for feed_url in RSS_FEEDS:

        try:
            feed = feedparser.parse(feed_url)

            for entry in feed.entries:

                title = entry.get("title", "").strip()
                link = entry.get("link", "").strip()

                # 🧠 جلوگیری از داده خراب
                if not title or not link:
                    continue

                image = extract_image(entry)

                all_news.append({
                    "title": title,
                    "link": link,
                    "image": image
                })

        except Exception as e:
            print("خطا در خواندن RSS:", e)

    return all_news