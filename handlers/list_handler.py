import os
from notion_client import Client
from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

async def list_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        num = int(context.args[0]) if context.args else 5
    except ValueError:
        await update.message.reply_text("❌ 格式錯誤，請使用 /list 或 /list 數字")
        return

    try:
        response = notion.databases.query(
            database_id=DATABASE_ID,
            sorts=[{"timestamp": "created_time", "direction": "descending"}],
            page_size=num
        )

        results = response.get("results", [])
        if not results:
            await update.message.reply_text("目前資料庫中沒有任何紀錄。")
            return

        reply_lines = []
        for i, page in enumerate(results, 1):
            props = page["properties"]
            title = props["Name"]["title"][0]["plain_text"] if props["Name"]["title"] else "（無書名）"
            author = props["Author"].get("select", {}).get("name", "未知作者")
            
            # 取得 created_time 並轉換格式
            created_iso = page.get("created_time", "")
            created_date = "未知時間"
            if created_iso:
                try:
                    dt = datetime.fromisoformat(created_iso.replace("Z", "+00:00"))
                    created_date = dt.strftime("%Y-%m-%d")
                except:
                    pass

            reply_lines.append(f"{i}. 《{title}》 by {author} ({created_date})")

        await update.message.reply_text("\n".join(reply_lines))

    except Exception as e:
        await update.message.reply_text(f"❌ 查詢 Notion 失敗：{e}")
