import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

TOKEN = os.getenv("TOKEN")
DEVELOPER = 844817222
ADMINS = []

BASE_WEBHOOK_URL = os.getenv("BASE_WEBHOOK_URL")

I18N_DOMAIN = 'lang'
LOCALES_DIR = 'locale'


CHANNELS = [
    {
        "name": "channel 1", 
        "link": "test_channeln66",
        "chat_id": 2799858045
    }
]

