import ccxt.async_support as ccxt
from abc import ABC, abstractmethod
from typing import Optional, Any


class ExchangeResponse:
    def __init__(self, result: Optional[Any], status: int, message: str):
        self.result = result
        self.status = status
        self.message = message

    def to_dict(self) -> dict:
        return {
            'result': self.result,
            'status': self.status,
            'message': self.message
        }

    def __str__(self) -> str:
        return f'ExchangeResponse(result={self.result}, status={self.status}, message={self.message})'


class BaseExchange(ABC):
    def __init__(self, api_key: str, api_secret: str, exchange_name: str, api_passphrase: str = None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase
        self.exchange_id = exchange_name

        exchange_class = getattr(ccxt, exchange_name)
        exchange_params = {
            'options': {'defaultType': 'spot'},
            'apiKey': api_key,
            'secret': api_secret,
        }

        if api_passphrase:
            exchange_params['password'] = api_passphrase

        self.exchange = exchange_class(exchange_params)

    @abstractmethod
    async def open_spot_market_orders(self, symbol: str, amount_usdt: float):
        pass

    async def get_free_balance(self, currency: str = 'USDT'):
        exchange_balance = await self.exchange.fetch_balance()
        usdt_free_balance = exchange_balance['free'].get(currency, 0)

        return usdt_free_balance

    async def close(self):
        await self.exchange.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

