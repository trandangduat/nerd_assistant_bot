import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(text = 'xin chao du ma ' + update.effective_chat.first_name + "🤓☝️", chat_id = update.effective_chat.id);

if __name__ == '__main__':
    application = ApplicationBuilder().token('7184210203:AAHh1ukQlfynmIPkgDb-6VIaF5Al0wjgfFc').build()
    
    application.add_handler(CommandHandler('hello', hello))
    
    application.run_polling()