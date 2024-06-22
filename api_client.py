# api_client.py

import requests
import time
import hmac
import base64
import json
from hashlib import sha256

class OKXClient:
    def __init__(self, api_key, secret_key, passphrase):
        # OKXClient 초기화 함수
        # API 키, 비밀 키, 패스프레이즈를 설정합니다.
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
        self.base_url = "https://www.okx.com"

    def _generate_signature(self, method, endpoint, body=''):
        # 요청의 서명을 생성하는 함수
        # API 요청에 필요한 서명을 생성합니다.
        timestamp = str(time.time())
        message = timestamp + method + endpoint + body
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message.encode('utf-8'), sha256).digest()
        return base64.b64encode(signature).decode()

    def _request(self, method, endpoint, params=None):
        # API 요청을 보내는 함수
        # 지정된 메서드와 엔드포인트로 API 요청을 보냅니다.
        url = self.base_url + endpoint
        headers = {
            'OK-ACCESS-KEY': self.api_key,
            'OK-ACCESS-SIGN': self._generate_signature(method, endpoint),
            'OK-ACCESS-TIMESTAMP': str(time.time()),
            'OK-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        }
        response = requests.request(method, url, headers=headers, json=params)
        return response.json()

    def get_ticker(self, instrument_id):
        # 티커 정보를 가져오는 함수
        # 지정된 상품 ID에 대한 현재 시세 정보를 가져옵니다.
        endpoint = f"/api/v5/market/ticker?instId={instrument_id}"
        return self._request('GET', endpoint)

    def get_candles(self, instrument_id, bar, limit):
        # 캔들 데이터를 가져오는 함수
        # 지정된 상품 ID에 대한 캔들 데이터를 가져옵니다.
        endpoint = f"/api/v5/market/candles?instId={instrument_id}&bar={bar}&limit={limit}"
        return self._request('GET', endpoint)

    def place_order(self, inst_id, side, ord_type, sz, px=None):
        # 주문을 생성하는 함수
        # 지정된 매개변수로 새로운 주문을 생성합니다.
        endpoint = "/api/v5/trade/order"
        body = {
            "instId": inst_id,
            "side": side,
            "ordType": ord_type,
            "sz": sz,
            "px": px
        }
        return self._request('POST', endpoint, body)
