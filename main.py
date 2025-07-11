import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from ai.yandex_gpt import generate_text
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "harmonious-charisma-production.up.railway.app")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="💬 Открыть AI-чат", web_app=WebAppInfo(url=WEBAPP_URL))
    ]])
    await message.answer("Привет! Нажми кнопку ниже, чтобы открыть веб-интерфейс.", reply_markup=keyboard)

@dp.message()
async def handle_message(message: Message):
    user_text = message.text
    reply = generate_text(user_text)
    await message.answer(reply)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
