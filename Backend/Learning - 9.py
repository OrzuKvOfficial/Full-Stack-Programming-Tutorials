import requests

# Telegram bot token va chat ID ni kiritish
token = 'YOUR_TELEGRAM_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'
text = 'Salom, bu Telegram orqali yuborilgan xabar!'

# Telegram API orqali xabar yuborish
url = f'https://api.telegram.org/bot{token}/sendMessage'
params = {'chat_id': chat_id, 'text': text}
requests.get(url, params=params)
