from rubtl_mega import RubTL, MegaConfig

# ایجاد نمونه از ربات
bot = RubTL(
    phone="YOUR_PHONE",
    session="t"
)

# هندلر پیام‌ها
@bot.on_message()
async def handle_message(client, message):
    if message.text == "/start":
        await client.send_message(
            message.chat.chat_id,
            f"""
👋 سلام به ربات مگا خوش آمدید!
🤖 ساخته شده با RubTL نسخه {MegaConfig.VERSION}
👨‍💻 سازنده: {MegaConfig.CREATOR}

📚 برای دیدن راهنما، /help را بزنید
            """
        )

# هندلر اینلاین
@bot.on_inline_query()
async def handle_inline(client, query):
    if query.query:
        results = [
            {
                "type": "article",
                "id": "1",
                "title": "ارسال با RubTL",
                "description": query.query,
                "input_message_content": {
                    "message_text": f"✨ {query.query}\n\n🤖 Powered by RubTL"
                }
            }
        ]
        await client.answer_inline_query(query.id, results)

# اجرای ربات
bot.run()
