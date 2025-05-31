import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
from handlers.add_handler import add_handler
from handlers.list_handler import list_handler
from handlers.search_handler import search_handler
from handlers.random_handler import random_handler
from handlers.count_handler import count_handler
from handlers.help_handler import help_handler
from handlers.unknown_handler import unknown_handler

load_dotenv()

if __name__ == '__main__':
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("add", add_handler))
    app.add_handler(CommandHandler("list", list_handler))
    app.add_handler(CommandHandler('search', search_handler))
    app.add_handler(CommandHandler('random', random_handler))
    app.add_handler(CommandHandler('count', count_handler))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(MessageHandler(filters.COMMAND, unknown_handler))

    print("🤖 Bot 已啟動...")
    app.run_polling()
