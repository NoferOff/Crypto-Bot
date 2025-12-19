# бібліотека
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder,CallbackQueryHandler,CommandHandler
from dotenv import load_dotenv
import os

load_dotenv()
# токен
ApplicationBuilder().token(os.getenv("BOT_TOKEN"))



# повідолення
markup = InlineKeyboardMarkup([
    [InlineKeyboardButton("📈 Show Prices", callback_data='show_prices')],
    [InlineKeyboardButton("💰 Check Balance", callback_data='check_balance')],
    [InlineKeyboardButton("⚙️ Settings", callback_data='settings')]
])
async def start(update, context):
   await update.message.reply_text("Hello! 👋\n"
        "I’m your Crypto-Bot 🤖\n"
        "I can show cryptocurrency prices, help check your balance, and perform actions.\n\n"
        "Click a button below to choose an action ⬇️", reply_markup=markup)
   


# кнопки
async def buttons(update, context):
    query = update.callback_query
    await query.answer()

# запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("Бот запущено...")
    app.run_polling()