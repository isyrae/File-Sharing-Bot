# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

import os
import logging
from logging.handlers import RotatingFileHandler

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "Add_Your_Token_Here")

#Your API ID HASH from my.telegram.org 
APP_ID = int(os.environ.get("APP_ID", "Add_Your_API_ID_Here"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "Add_Your_API_HASH_Here")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "Add_Your_Channel_ID_Here"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "Add_Your_Owner_ID_Here"))

#Port
PORT = os.environ.get("PORT", "8585")

#Database 
DB_URI = "mongodb://127.0.0.1:27017"
DB_NAME = "filebot"

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "You_ShortLink_Provider_URL")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "Add_Your_ShortLink_API_Here")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/isyrae") # You can add here your tutorial video

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "Add_Your_ForceSub_Channel"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We LeakHubd or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

ADMINS.append(OWNER_ID)
ADMINS.append(1234567890)

LOG_FILE_NAME = "filebot.txt"

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

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

