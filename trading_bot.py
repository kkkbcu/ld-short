# trading_bot.py

class TradingBot:
    def __init__(self, client, strategy):
        # TradingBot 초기화 함수
        # API 클라이언트와 거래 전략을 설정합니다.
        self.client = client
        self.strategy = strategy

    def execute_trade(self, instrument_id):
        # 거래를 실행하는 함수
        # EMA 전략을 기반으로 매수/매도 신호를 받아서 거래를 실행합니다.
        signal = self.strategy.ema_strategy(instrument_id, short_window=12, long_window=26)
        if signal == "buy":
            self.client.place_order(inst_id=instrument_id, side='buy', ord_type='market', sz='1')
            print("Buy order placed.")
        elif signal == "sell":
            self.client.place_order(inst_id=instrument_id, side='sell', ord_type='market', sz='1')
            print("Sell order placed.")
        else:
            print("No trade executed.")
