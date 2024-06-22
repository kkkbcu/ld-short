# trading_strategy.py

import numpy as np

class TradingStrategy:
    def __init__(self, client):
        # TradingStrategy 초기화 함수
        # API 클라이언트를 설정합니다.
        self.client = client

    def ema(self, prices, window):
        # EMA 계산 함수
        # 주어진 가격 데이터와 윈도우 크기를 이용하여 EMA를 계산합니다.
        if len(prices) < window:
            raise ValueError("Price data is not sufficient for EMA calculation.")

        weights = np.exp(np.linspace(-1., 0., window))
        weights /= weights.sum()
        ema = np.convolve(prices, weights, mode='full')[:len(prices)]
        ema[:window] = ema[window]
        return ema


    def ema_strategy(self, instrument_id, short_window, long_window):
        # EMA 전략을 실행하는 함수
        # 1분봉 데이터를 조회하고, 단기 EMA와 장기 EMA를 계산하여 매수/매도 신호를 반환합니다.
        candle_data = self.client.get_candles(instrument_id, '1m', max(short_window, long_window))
        prices = [float(candle[4]) for candle in candle_data['data']]  # 종가 리스트

        try:
            short_ema = self.ema(prices, short_window)[-1]
            long_ema = self.ema(prices, long_window-1)[-1]

        except ValueError as e:
            print(f"EMA calculation error: {e}")
            return "hold"

        if short_ema > long_ema:
            return "buy"
        elif short_ema < long_ema:
            return "sell"
        else:
            return "hold"
