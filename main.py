from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Nice to meet you!I")

if __name__ == "__main__":
    app = ApplicationBuilder().token("0").build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Бот запущено...")
    app.run_polling()
