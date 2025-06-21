import os
import datetime
import asyncio
import json
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from mood_utils import detect_mood, save_mood_log

BOT_TOKEN = "8192250077:AAE8en1Xl-3dYC0SKXwMjBq4iuvV_bxS2Jw"
user_reminders = {}
scheduler = AsyncIOScheduler()

# --- Telegram Handlers ---
async def start(update, context):
    await update.message.reply_text("Hi! 🌸 I'm your Mental Health Buddy.\nTell me, how are you feeling today?")

async def handle_message(update, context):
    text = update.message.text
    user_id = update.message.chat_id
    mood = detect_mood(text)
    save_mood_log(user_id, mood, text)
    await update.message.reply_text(f"Got it! You're feeling: {mood}")

async def set_reminder(update, context):
    user_id = update.message.chat_id
    try:
        time = context.args[0]  # format HH:MM
        hour, minute = map(int, time.split(":"))
        user_reminders[user_id] = {"hour": hour, "minute": minute}
        scheduler.add_job(send_reminder, CronTrigger(hour=hour, minute=minute), args=[context.bot, user_id], id=str(user_id), replace_existing=True)
        await update.message.reply_text(f"⏰ Daily mood summary reminder set for {time}!")
    except Exception as e:
        await update.message.reply_text("❌ Usage: /setreminder HH:MM")

async def send_reminder(bot, user_id):
    await bot.send_message(chat_id=user_id, text="🧠 It's time for your daily mood check-in! How are you feeling today?")

# --- Main Run Loop ---
async def main():
    scheduler.start()
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setreminder", set_reminder))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running... Press Ctrl+C to stop.")
    await app.run_polling()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError:
        import nest_asyncio
        nest_asyncio.apply()
        asyncio.get_event_loop().run_until_complete(main())
