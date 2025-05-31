# BookToNotionBot

一個用來將書名與作者快速寫入 Notion 資料庫的 Telegram Bot。

---

## 功能指令

| 指令 | 說明 |
| --- | --- | 
| `/add 書名 作者` | 新增一本書 (書名與作者間以換行隔開) |
| `/list n`     | 顯示最近 n 筆書籍（預設 5 筆） |
| `/search 關鍵字` | 搜尋書名或作者 |
| `/random`       | 隨機推薦一本書 |
| `/count`        | 顯示書籍總數 |
| `/help`         | 顯示說明 |

---

## 安裝步驟

1. Create Fork
2. 建立 Railway 專案
   1. 前往 https://railway.app 並登入
   2. 點選 `New Project` → 選擇 `Deploy from GitHub repo`
   3. 選擇 `BookToNotionBot` 專案

3. 設定環境變數
   1. 點右側 `Variables`
   2. 新增以下三個變數
      1. `TELEGRAM_BOT_TOKEN`
      
          在 Telegram 使用 [@BotFather](https://t.me/botfather) 建立 Telegram Bot 並獲得 token         

      2. `NOTION_DATABASE_ID`

          從 Notion 資料庫頁面中獲取網址，複製 `https://www.notion.so/` 後 `?` 前的 32 字元

          Ex: `https://www.notion.so/20483fa865128XXXXX23cbf8cb2ef0a4?v=2048...` 的資料庫ID是 `20483fa865128XXXXX23cbf8cb2ef0a4`

      3. `NOTION_TOKEN`

          進入 [Notion/Integrations](https://www.notion.so/profile/integrations) 新增 integration

          將其加入目標資料庫的 Connection 中
4. 部署並執行
   - Railway 會自動部署並執行 `main.py`
   - 點 `Deployment` 可查看 log（包含 bot 是否啟動成功）

---

## Notion 資料庫格式要求

| Name | Author | 
| ---- | ------ |
| 書名 | 作者 | 

--- 

## 結構

```
BookToNotionBot/
├── main.py                     # 主程式，啟動 Telegram Bot
└── handlers/                   # 各功能的獨立處理模組
    ├── __init__.py             # 空檔（保留為 Python 模組）
    ├── add_handler.py          # 處理 /add 指令
    ├── list_handler.py         # 處理 /list 指令
    ├── search_handler.py       # 處理 /search 指令
    ├── random_handler.py       # 處理 /random 指令
    ├── count_handler.py        # 處理 /count 指令
    ├── help_handler.py         # 處理 /help 指令
    └── unknown_handler.py      # 處理未知指令
```