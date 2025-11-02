import os
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

load_dotenv()

async def start(update, context):
    await update.message.reply_text("BOTUL TĂU ESTE ACUM ÎN CLOUD!\nRulează 24/7\nChromebook = LIBER")

if __name__ == "__main__":
    app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    print("BOTUL RULEAZĂ...")
    app.run_polling()
