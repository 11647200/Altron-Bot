import asyncio
from random import choice

from pyrogram.types import Message
from pyrogram import filters, Client
from config import SUDO_USERS
from helpers.data import GROUP, PORMS


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["spam", "spamming"], [".", "!", "/"]))
async def suspam(client: Client, message: Message):
    quantity = int(message.text.split(" ", 2)[1])
    spam_text = ' '.join(message.command[2:])

    if message.reply_to_message:
        spam_text = message.reply_to_message.text
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text)
            await asyncio.sleep(0.3)
    elif len(spam_text) > 0:
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text)
            await asyncio.sleep(0.3)
    else:
        await message.reply_text("😈 Usage:\n !spam 13 Altron")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["fastspam", "fspam"], [".", "!", "/"]))
async def spspam(client: Client, message: Message):
    quantity = int(message.text.split(" ")[1])
    spam_text = ' '.join(message.command[2:])
    
    if message.reply_to_message:
        spam_text = message.reply_to_message.text
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text)
            await asyncio.sleep(0.001)
    elif len(spam_text) > 0:
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text)
            await asyncio.sleep(0.001)
    else:
        await message.reply_text("😈 Usage:\n !fspam 11 Altron")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], [".", "!", "/"]))
async def pussy(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("**reply to a sticker with amount you want to spam**")
        return
    if not message.reply_to_message.sticker:
        await message.edit_text(text="**reply to a sticker with amount you want to spam**")
        return
    else:
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.2)

        if message.chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.2)


@Client.on_message(filters.command(["pspam", "pornspam"], [".", "/", "!"]) & filters.user(SUDO_USERS))
async def pspam(client: Client, message: Message):
    if int(message.chat.id) in GROUP:
        await message.reply_text("» ꜱᴏʀʀʏ, ᴛʜɪꜱ ɪꜱ ᴀʟᴛʀᴏɴ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ.")
        return

    quantity = message.text.split(" ")[1]
    for _ in range(quantity):
        PORM = choice(PORMS)
        await client.send_video(message.chat.id, PORM)
        await asyncio.sleep(0.3)
    else:
        await message.reply_text("🔞 Usage:\n !pspam 10")


@Client.on_message(filters.command('join', [".", "!", "/"]) & filters.user(SUDO_USERS))
async def fuck(client: Client, message: Message):
    hero = message.text[6:]
    if not hero:
        return await message.reply_text("Need a chat username or invite link to join.")
    if hero.isnumeric():
        return await message.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        await client.join_chat(hero)
        await message.reply_text(f"**Joined ✅**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command('leave', [".", "!", "/"]) & filters.user(SUDO_USERS))
async def leftfuck(client: Client, message: Message):
    hero = message.text[6:]
    if not hero:
        return await message.reply_text("Need a chat username or invite link to leave.")
    if hero.isnumeric():
        return await message.reply_text("Can't leave a chat with chat id. Give username or invite link.")
    try:
        await client.leave_chat(hero)
        await message.reply_text(f"**Left ❌**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
