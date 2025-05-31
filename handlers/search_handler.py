import os
from notion_client import Client
from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

async def search_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("請輸入要搜尋的關鍵字，例如：\n/search priest")
        return

    keyword = " ".join(context.args).lower()

    try:
        response = notion.databases.query(database_id=DATABASE_ID)
        results = response.get("results", [])

        matches = []
        for page in results:
            props = page["properties"]
            title = props["Name"]["title"][0]["plain_text"] if props["Name"]["title"] else ""
            author = props["Author"].get("select", {}).get("name", "")

            if keyword in title.lower() or keyword in author.lower():
                matches.append(f"《{title}》 by {author}")

        if matches:
            await update.message.reply_text("🔍 搜尋結果：\n" + "\n".join(matches))
        else:
            await update.message.reply_text("❌ 查無資料")

    except Exception as e:
        await update.message.reply_text(f"❌ 搜尋失敗：{e}")
