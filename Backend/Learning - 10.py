from pyrogram import Client

api_id = 123456  # O'zingiz olgan API ID
api_hash = "your_api_hash"  # O'zingiz olgan API Hash

app = Client("my_account", api_id=api_id, api_hash=api_hash)

with app:
    app.send_message("me", "Salom, bu bot orqali jo'natilgan xabar!")
