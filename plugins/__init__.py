# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

from aiohttp import web
from .route import routes

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────
