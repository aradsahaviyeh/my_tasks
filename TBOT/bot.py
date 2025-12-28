from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters,
)
from os import environ
from dotenv import load_dotenv

load_dotenv()
_token = environ["TOKEN"]


# for start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello welcome to this Bot")


# for help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can read the guide at www.help.com")


# for any text
async def static_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello how can I help you ?")


if __name__ == "__main__":
    app = ApplicationBuilder().token(_token).build()

    # commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), static_message))

    app.run_polling()