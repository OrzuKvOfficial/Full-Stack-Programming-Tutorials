from instabot import Bot

# Instagram hisobingizga ulaning
bot = Bot()
bot.login(username='YOUR_USERNAME', password='YOUR_PASSWORD')

# Xabar yuborish
recipient_username = 'RECIPIENT_USERNAME'
message = 'Salom, bu Python orqali yuborilgan xabardir!'

bot.send_message(message, [recipient_username])
