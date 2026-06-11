import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

ICP_URL = "https://icp.administracionelectronica.gob.es/icpplus/acOpcDirect"

if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN is not configured")

if not TELEGRAM_CHAT_ID:
    raise ValueError("TELEGRAM_CHAT_ID is not configured")
