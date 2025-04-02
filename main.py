import requests
import telebot
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # دریافت توکن از متغیر محیطی
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # دریافت Chat ID

bot = telebot.TeleBot(TOKEN)

def find_memecoins():
    url = "https://api.dextools.io/v1/pair/search?query=meme"
    headers = {"Authorization": "Bearer YOUR_DEXTOOLS_API_KEY"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data["pairs"]:
            first_pair = data["pairs"][0]
            message = f"🚀 پامپ جدید پیدا شد!\n🔹 نماد: {first_pair['symbol']}\n💰 قیمت: {first_pair['price']}$"
            bot.send_message(CHAT_ID, message)
