import requests
import os
import time

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_telegram_message():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": "הודעה כל דקה מגיטהאב 🚀"}
    requests.post(url, data=payload)

if __name__ == "__main__":
    while True:
        send_telegram_message()
        time.sleep(60)
