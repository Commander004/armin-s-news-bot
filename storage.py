import json
import os

from config import SENT_NEWS_FILE


def load_sent_news():

    if not os.path.exists(SENT_NEWS_FILE):

        with open(SENT_NEWS_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)

        return set()

    try:

        with open(SENT_NEWS_FILE, "r", encoding="utf-8") as file:

            data = json.load(file)

            return set(data)

    except Exception:

        return set()


def save_sent_news(sent_news):

    with open(SENT_NEWS_FILE, "w", encoding="utf-8") as file:

        json.dump(list(sent_news), file, ensure_ascii=False, indent=4)