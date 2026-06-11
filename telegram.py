import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_message(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    response = requests.post(
        url,
        json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
        },
        timeout=30,
    )
    response.raise_for_status()
