# backtesting.py

import matplotlib.pyplot as plt

class Backtesting:
    def __init__(self, client, strategy):
        # Backtesting 초기화 함수
        self.client = client
        self.strategy = strategy

    def run(self, instrument_id, short_window, long_window, start_time, end_time):
        # 백테스팅을 실행하는 함수
        candle_data = self.client.get_candles(instrument_id, '1m', 1000)  # 필요한 데이터 양에 맞게 조절
        prices = [float(candle[4]) for candle in candle_data['data']]

        short_ema = self.strategy.ema(prices, short_window)
        long_ema = self.strategy.ema(prices, long_window)

        signals = []
        for short, long in zip(short_ema, long_ema):
            if short > long:
                signals.append("buy")
            elif short < long:
                signals.append("sell")
            else:
                signals.append("hold")

        # 결과 시각화
        plt.figure(figsize=(14, 7))
        plt.plot(prices, label='Price')
        plt.plot(short_ema, label='Short EMA')
        plt.plot(long_ema, label='Long EMA')
        plt.title('Backtesting Results')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

        return signals

