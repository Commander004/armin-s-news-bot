import time
import random

from rss_reader import get_news
from storage import load_sent_news, save_sent_news
from sender import send_message, send_photo
from utils import add_emoji
from ai import translate_news


def run():

    print("🚀 AutoNewsBot Started...")

    sent_news = set(load_sent_news())

    while True:

        try:

            news_list = get_news()

            if not news_list:
                print("⚠️ خبر جدیدی پیدا نشد، یک دقیقه دیگر دوباره بررسی می‌کنم...")
                time.sleep(60)
                continue

            new_sent = False

            for latest_news in news_list:

                link = latest_news.get("link", "").strip()
                title = latest_news.get("title", "").strip()
                image = latest_news.get("image")

                if not link or not title:
                    continue

                # اگر قبلاً ارسال شده
                if link in sent_news:
                    continue

                print("📰 خبر جدید پیدا شد")

                title = add_emoji(translate_news(title))
                message = f"{title}\n- [x] *@akhbartareek*"

                valid_image = (
                    isinstance(image, str)
                    and image.startswith("http")
                )

                try:
                    if valid_image:
                        status = send_photo(image, message)
                    else:
                        status = send_message(message)
                except Exception as send_error:
                    print("❌ خطا در ارسال:", send_error)
                    status = None

                if status == 200:

                    print("✅ خبر ارسال شد")

                    sent_news.add(link)
                    save_sent_news(list(sent_news))

                    new_sent = True
                    break

                else:
                    print("❌ ارسال ناموفق بود")

            if new_sent:

                sleep_time = random.choice([300, 600])
                print(f"⏳ {sleep_time} ثانیه صبر می‌کنم...")
                time.sleep(sleep_time)

            else:
                # هیچ خبر جدیدی ارسال نشد
                print("ℹ️ خبر جدیدی برای ارسال نبود، یک دقیقه دیگر دوباره بررسی می‌کنم...")
                time.sleep(60)

        except Exception as e:

            print("❌ خطا:", e)
            print("⏳ یک دقیقه دیگر دوباره تلاش می‌کنم...")
            time.sleep(60)


if __name__ == "__main__":
    run() 