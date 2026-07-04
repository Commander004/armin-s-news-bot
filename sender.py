import requests
from config import BOT_TOKEN, CHANNEL_ID


def send_message(text):
    try:
        url = f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage"

        data = {
            "chat_id": CHANNEL_ID,
            "text": text
        }

        response = requests.post(url, data=data, timeout=10)
        return response.status_code

    except Exception as e:
        print("❌ خطا در send_message:", e)
        return None


def send_photo(photo_url, caption):
    try:
        # 🧠 امنیت عکس
        if not photo_url or not isinstance(photo_url, str):
            return send_message(caption)

        url = f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendPhoto"

        data = {
            "chat_id": CHANNEL_ID,
            "photo": photo_url,
            "caption": caption
        }

        response = requests.post(url, data=data, timeout=10)
        return response.status_code

    except Exception as e:
        print("❌ خطا در send_photo:", e)
        # اگر عکس مشکل داشت → fallback به متن
        return send_message(caption)