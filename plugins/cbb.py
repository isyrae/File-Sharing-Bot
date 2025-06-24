# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://github.com/isyrae/File-Sharing-Bot'>Click here</a>\n○ Channel : @isyrae\n○ Support Group : @isyraeprojects</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

