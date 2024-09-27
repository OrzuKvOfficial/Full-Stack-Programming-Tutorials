from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# "/start" komandasi uchun ishlatiladigan funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!')

if __name__ == '__main__':
    # Bot tokenini kiritamiz
    application = ApplicationBuilder().token('YOUR_BOT_TOKEN').build()

    # "start" komandasi uchun handler yaratamiz
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Botni ishga tushiramiz
    application.run_polling()
