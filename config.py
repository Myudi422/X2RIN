import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1912233708:AAHLpkitj3fmDplit-rMa7uPkCrA84_xF1s")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7120601"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "aebd45c2c14b36c2c91dec3cf5e8ee9a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001448249578"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "784985038"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://npshqryw:qB36Hl2d64csE9t2-GpFPeu03XPICiLA@hansken.db.elephantsql.com/npshqryw")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001546083133"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hai {first} <b>untuk menggunakan bot ini, silahkan subscribe channel kami terlebih dahulu.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append("784985038, 1808809023")

LOG_FILE_NAME = "filesharingbot.txt"

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
