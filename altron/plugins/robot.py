import heroku3

from datetime import datetime
from pyrogram import filters, Client
from config import *


@Client.on_message(filters.command(["ping"], ["/", ".", "!"]) & filters.user(SUDO_USERS))
async def ping(Client, message):
    start = datetime.now()
    loda = await message.reply_text("» __ᴀʟᴛʀᴏɴ__")
    end = datetime.now()
    mp = (end - start).microseconds / 1000
    await loda.edit_text(f"__🤖 ᴘɪɴɢ__\n» `{mp} ms`")


Heroku = heroku3.from_key(HEROKU_API_KEY)
sudousers = os.environ.get("SUDO_USERS", None)

@Client.on_message(filters.command(["sudo"], ["/", ".", "!"]) & filters.user(OWNER_ID))
async def addsudo(xspam: Client, message):
    evil = await message.reply_text(f"» __ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...__")
    target = ""
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await evil.edit_text("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
        return
    heroku_var = app.config()
    if message is None:
        return
    try:
        user_id = message.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        target = ok.id
    except Exception:
        await evil.edit_text("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!")
    if len(sudousers) > 0:
        newsudo = f"{sudousers} {target}"
    else:
        newsudo = f"{target}"
    await evil.edit_text(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
    if str(target) not in sudousers:
        heroku_var["SUDO_USERS"] = newsudo
