# main.py

import asyncio
from api_client import OKXClient
from trading_strategy import TradingStrategy
from trading_bot import TradingBot
from telegram_bot import TelegramBot
from backtesting import  Backtesting

async def main():
    # API 키, 비밀 키, 패스프레이즈 설정
    api_key = "1751a30a-01cb-4df3-a0be-36b39f40eaeb"
    secret_key = "B7B496A993DB1AF825621B00118EF689"
    passphrase = "@Ss0107739"

    # 텔레그램 봇 설정
    telegram_token = "6572201072:AAF5BbXTC3JJrVqLLbyYwIUZbiZ9ErIQceE"
    telegram_chat_id = "6981481834"

    # 클라이언트, 전략, 봇, 텔레그램 봇 초기화
    client = OKXClient(api_key, secret_key, passphrase)
    strategy = TradingStrategy(client)
    bot = TradingBot(client, strategy)
    telegram_bot = TelegramBot(telegram_token, telegram_chat_id)

    # 거래 실행 및 텔레그램 알림
    instrument_id = "ETH-USDT"
    signal = strategy.ema_strategy(instrument_id, short_window=12, long_window=26)
    if signal in ["buy", "sell"]:
        bot.execute_trade(instrument_id)
        await telegram_bot.send_message(f"Trade executed: {signal} {instrument_id}")


    # 백테스팅 실행
    backtesting = Backtesting(client, strategy)
    backtesting.run(instrument_id, short_window=12, long_window=26, start_time='2022-01-01', end_time='2022-12-31')


if __name__ == "__main__":
    asyncio.run(main())