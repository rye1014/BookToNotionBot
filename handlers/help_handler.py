from telegram import Update
from telegram.ext import ContextTypes

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "📚 *可用指令列表：*\n\n"
        "/add 書名↵作者\n"
        "  新增一本書到資料庫\n\n"
        "/list [n]\n"
        "  列出最近新增的 n 本書（預設 5 本）\n\n"
        "/search 關鍵字\n"
        "  搜尋書名或作者中含有關鍵字的資料\n\n"
        "/random\n"
        "  隨機推薦一本書\n\n"
        "/count\n"
        "  顯示目前書籍總數\n\n"
        "/help\n"
        "  顯示這份說明"
    )

    await update.message.reply_text(help_text, parse_mode="Markdown")
