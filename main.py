from config import *
from pyrogram import idle


CLIENTS = []

for SESSION in SESSIONS:
    if SESSION:
        client = Client(
            session_name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="TheXSpam"),
        )
        CLIENTS.append(client)


if __name__ == "__main__":

    for i, CLIENT in enumerate(CLIENTS):
        try:
            CLIENT.start()
            CLIENT.join_chat("TheAltron")
            CLIENT.join_chat("AltronChats")
            print(f"---> Client {i+1} has been Started...")
        except Exception as e:
            print(e)

    print("💞YOUR PY-ALTRON SPAM USERBOTS DEPLOYED SUCCESSFULLY 💞")
    idle()
