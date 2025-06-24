# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────

from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("isyrae")

# ──────────────────────────────────────────────────────────
#  📦 File Sharing Token Bot
#  🛠️ Developer : Rahul Mondal  |  📬 @isyrae
#  💁‍♂️ Telegram  : https://telegram.me/isyrae
#  📝 License   : MIT License — Use, Modify & Share Freely
# ──────────────────────────────────────────────────────────
