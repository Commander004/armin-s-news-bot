import re


def clean_text(text):
    """
    تمیز کردن متن خبر
    """

    if not text:
        return ""

    text = re.sub(r"\s+", " ", text)
    return text.strip()


def add_emoji(title: str):
    """
    اضافه کردن ایموجی بر اساس موضوع خبر
    """

    text = title.lower()

    if any(x in text for x in ["جنگ", "حمله", "انفجار", "درگیری", "فوری"]):
        return "🚨 " + title

    elif any(x in text for x in ["اینترنت", "فیلتر", "اختلال", "قطعی"]):
        return "🌐 " + title

    elif any(x in text for x in ["دلار", "ارز", "طلا", "سکه", "بازار"]):
        return "💵 " + title

    elif any(x in text for x in ["فوتبال", "ورزش", "استقلال", "پرسپولیس", "لیگ"]):
        return "⚽ " + title

    elif any(x in text for x in ["کالا", "کالابرگ", "یارانه", "معیشت"]):
        return "🛒 " + title

    elif any(x in text for x in ["نفت", "بنزین", "گاز", "انرژی"]):
        return "⛽ " + title

    elif any(x in text for x in ["دولت", "مجلس", "رئیس", "قانون"]):
        return "🏛 " + title

    else:
        return "🔴 " + title


def format_news(title):
    """
    قالب نهایی خبر (بدون فاصله اضافه و بدون ایموجی اضافی)
    """

    return f"{title}\n- [x] *@akhbartareek*"