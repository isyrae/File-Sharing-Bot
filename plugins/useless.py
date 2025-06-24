# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT,ADMINS
from datetime import datetime
from helper_func import get_readable_time
from database.database import add_user, present_user

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

@Bot.on_message(filters.private & filters.incoming)
async def useless(_,message: Message):
    id = message.from_user.id
    owner_id = ADMINS 


    if id == owner_id:
        await message.reply("You are the owner! Additional actions can be added here.")

    else:
        if not await present_user(id):
            try:
                await add_user(id)
            except:
                pass
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

