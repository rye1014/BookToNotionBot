from telegram import Update
from telegram.ext import ContextTypes

async def unknown_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❓ 未知指令。請輸入 /help 查看可用指令。")
