import requests
import os
import time

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

counter = 7
words = ["אחד", "שני", "שלושה", "ארבעה", "חמישה", "שישה"]
def send_telegram_message():
    global counter
    global words
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"לא לשכוח ספירת העומר\nהיום {counter} ימים לעומר שהם {words[counter//7 - 1]} שבועות{counter%7 != 0 and f" ו{words[counter%7 - 1]} ימים" or ''}"}
    counter += 1
    requests.post(url, data=payload)

if __name__ == "__main__":
    send = False
    while True:
        if time.localtime().tm_sec == 0:
            if not send:
                send = True
                send_telegram_message()
        else:
            send = False
