import requests
import os
import time

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_telegram_message():
    counter = 7
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"לא לשכוח ספירת העומר \n היום {counter} ימים לעומר שהם {counter/7} שבועות ו{counter%7} ימים"}
    counter += 1
    requests.post(url, data=payload)

if __name__ == "__main__":
    while True:
        if time.localtime().tm_hour == 2 and (time.localtime().tm_min == 55 or time.localtime().tm_min == 56):
            send_telegram_message()
