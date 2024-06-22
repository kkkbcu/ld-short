# telegram_bot.py

from telegram import Bot
import asyncio

class TelegramBot:
    def __init__(self, token, chat_id):
        # TelegramBot 초기화 함수
        self.bot = Bot(token=token)
        self.chat_id = chat_id

    async def send_message(self, message):
        # 메시지를 보내는 함수
        await self.bot.send_message(chat_id=self.chat_id, text=message)
