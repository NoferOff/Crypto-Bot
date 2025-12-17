from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler,MessageHandler

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 👋\n"
        "I’m your Crypto-Bot 🤖\n"
        "I can show cryptocurrency prices, help check your balance, and perform actions.\n\n"
        "Click a button below to choose an action ⬇️")

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Бот запущено...")




    KeyboardInterrupt