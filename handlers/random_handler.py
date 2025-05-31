import os
import random
from notion_client import Client
from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

async def random_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = notion.databases.query(database_id=DATABASE_ID)
        results = response.get("results", [])

        if not results:
            await update.message.reply_text("資料庫是空的，無法隨機選擇。")
            return

        page = random.choice(results)
        props = page["properties"]
        title = props["Name"]["title"][0]["plain_text"] if props["Name"]["title"] else "（無書名）"
        author = props["Author"].get("select", {}).get("name", "未知作者")

        await update.message.reply_text(f"🎲 隨機推薦：\n《{title}》 by {author}")

    except Exception as e:
        await update.message.reply_text(f"❌ 查詢 Notion 失敗：{e}")
