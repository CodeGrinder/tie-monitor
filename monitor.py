import requests
from bs4 import BeautifulSoup

from config import ICP_URL
from telegram import send_message

def check_site():
    response = requests.get(
        ICP_URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(separator=" ", strip=True).lower()

def main():
    content = check_site()

    unavailable_phrases = [
        "en este momento no hay citas disponibles",
        "no hay citas disponibles",
    ]

    available = not any(p in content for p in unavailable_phrases)

    if available:
        send_message(
            "🚨 Posible disponibilidad detectada en ICPPlus. Revisa la web."
        )
        print("Availability detected")
    else:
        print("No availability")

if __name__ == "__main__":
    main()
