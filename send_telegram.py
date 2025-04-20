import requests
import os
import time

# BOT_TOKEN = os.environ["BOT_TOKEN"]
# CHAT_ID = os.environ["CHAT_ID"]
BOT_TOKEN = '7871293487:AAEI-73NZUgtLD264QoKJ-Vya4kbCWZnLOM'
CHAT_ID = 395009331
counter = 7
words = ["אחד", "שני", "שלושה", "ארבעה", "חמישה", "שישה"]
def send_telegram_message():
    global counter
    global words
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"לא לשכוח ספירת העומר\nהיום {counter} ימים לעומר שהם {words[counter//7]} שבועות ו{words[counter%7]} ימים"}
    counter += 1
    requests.post(url, data=payload)

if __name__ == "__main__":
    while True:
        if time.localtime().tm_hour == 3 and (time.localtime().tm_min == 19 or time.localtime().tm_min == 20) and time.localtime().tm_sec == 0:
            send_telegram_message()
