import os
from notion_client import Client
from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

async def count_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = notion.databases.query(database_id=DATABASE_ID)
        total = len(response.get("results", []))
        await update.message.reply_text(f"📚 目前已記錄 {total} 本書")
    except Exception as e:
        await update.message.reply_text(f"❌ 查詢失敗：{e}")
