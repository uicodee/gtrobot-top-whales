from .entities import BinanceExchange, BybitExchange, MexcExchange, BitgetExchange, OkxExchange


class ExchangeController:
    def __init__(self, exchange_name: str, api_key: str, api_secret: str, api_passphrase: str = None):
        self.exchange_name = exchange_name.lower()
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase
        self.exchange = None

    async def __aenter__(self):
        if self.exchange_name == 'binance':
            self.exchange = BinanceExchange(
                api_key=self.api_key,
                api_secret=self.api_secret,
                api_passphrase=self.api_passphrase
            )

        elif self.exchange_name == 'bybit':
            self.exchange = BybitExchange(
                api_key=self.api_key,
                api_secret=self.api_secret,
                api_passphrase=self.api_passphrase
            )

        elif self.exchange_name == 'mexc':
            self.exchange = MexcExchange(
                api_key=self.api_key,
                api_secret=self.api_secret,
                api_passphrase=self.api_passphrase
            )

        elif self.exchange_name == 'bitget':
            self.exchange = BitgetExchange(
                api_key=self.api_key,
                api_secret=self.api_secret,
                api_passphrase=self.api_passphrase
            )

        elif self.exchange_name == 'okx':
            self.exchange = OkxExchange(
                api_key=self.api_key,
                api_secret=self.api_secret,
                api_passphrase=self.api_passphrase
            )

        else:
            raise ValueError(f"Биржа '{self.exchange_name}' не поддерживается.")

        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.exchange:
            await self.exchange.close()

    async def open_spot_market_orders(self, symbols: list[str], amount_usdt: float):
        """
        :param symbols: List of crypto pairs: e.g. ['BTC/USDT', 'ETH/USDT'].
        :param amount_usdt: Total amount of USDT.
        """
        if not self.exchange:
            raise RuntimeError("Экземпляр биржи не инициализирован.")

        return await self.exchange.open_spot_market_orders(symbols, amount_usdt)

    async def get_free_balance(self, currency: str = 'USDT'):
        """
        :param currency: e.g. 'USDT'.
        """
        if not self.exchange:
            raise RuntimeError("Экземпляр биржи не инициализирован.")

        return await self.exchange.get_free_balance(currency)
