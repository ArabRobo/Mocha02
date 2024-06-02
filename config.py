import sys
import os
import logging
from logging.handlers import RotatingFileHandler


from dotenv import load_dotenv

load_dotenv("config.env")

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7363047700:AAHde9Y3KdEVQCA5uFMO_pvBdF2konFvf1I")
APP_ID = int(os.environ.get("APP_ID", "26730559"))
API_HASH = os.environ.get("API_HASH", "54e0fd326f54b4ea91fdcbdf98e3cf4e")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002179562284"))
OWNER_ID = int(os.environ.get("OWNER_ID", "5908553001"))
PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("DB_URI", "mongodb+srv://onedayubot:fadhil123@cluster0.44vvqsq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "geezfsub")
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001970835627"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001660822900"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001266185679"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "Hallo {first}\n\nsaya bisa menyimpan file dan membagikan dengan mudah.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5908553001").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hallo {first}\n\n<b>anda harus bergabung ke Channel/Group saya dulu untuk bisa melihat konten ini\n\nJoin Channel/group</b>")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False
try:
    import geezlibs
except ModuleNotFoundError:
    print("GeezLibs not installed, you are gay")
    sys.exit()
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Jangan kirimkan saya pesan!"

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "geezfsub.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
