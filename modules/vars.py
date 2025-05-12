import os

API_ID    = os.environ.get("API_ID", "24602445")
API_HASH  = os.environ.get("API_HASH", "180adef97e5d2f8a246f59280ce625b5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7664551221:AAEGGBRZKrLizNPp3oWzZTU4_wTTD4A9OJk") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
