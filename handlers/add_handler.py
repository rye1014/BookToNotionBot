import os
from notion_client import Client
from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv

load_dotenv()
notion = Client(auth = os.getenv('NOTION_TOKEN'))
DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

async def add_handler(update: Update, context = ContextTypes.DEFAULT_TYPE): 
    lines = update.message.text.split('\n')
    if len(lines) < 2: 
        await update.message.reply_text("請使用正確格式：\n/add 書名\n作者")
        return
    
    title = lines[0][5:].strip()
    author = lines[1].strip()

    try: 
        notion.pages.create(
            parent = {'database_id': DATABASE_ID}, 
            properties = {
                'Name': {
                    'title': [{'text': {'content': title}}]
                }, 
                'Author': {
                    'select': {'name': author}
                }
            }
        )
        await update.message.reply_text(f'✅ 已新增《{title}》 by {author}')

    except Exception as e: 
        await update.message.reply_text(f"❌ 寫入 Notion 失敗：{e}")
