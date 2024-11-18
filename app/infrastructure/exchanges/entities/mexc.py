from .base import BaseExchange, ABC, ExchangeResponse


class MexcExchange(BaseExchange, ABC):
    def __init__(self, api_key: str, api_secret: str, api_passphrase: str = None):
        super().__init__(
            api_key=api_key, api_secret=api_secret, api_passphrase=api_passphrase,
            exchange_name='mexc'
        )

    async def open_spot_market_orders(self, symbols: list[str], amount_usdt: float):
        try:
            markets = await self.exchange.load_markets()

            unsupported_symbols = []
            for symbol in symbols:
                if symbol not in markets:
                    unsupported_symbols.append(symbol)
                    continue

                if not markets[symbol]['info']['isSpotTradingAllowed']:
                    unsupported_symbols.append(symbol)

            if unsupported_symbols:
                return ExchangeResponse(
                    result=None,
                    status=422,
                    message=f'Следующие символы не поддерживаются: {unsupported_symbols}'
                )

            exchange_balance = await self.get_free_balance('USDT')
            if exchange_balance < amount_usdt:
                return ExchangeResponse(
                    result=None,
                    status=402,
                    message=f'Недостаточно средств для открытия сделок: {exchange_balance} USDT'
                )

            order_amount = amount_usdt / len(symbols)
            if order_amount < 10:
                return ExchangeResponse(
                    result=None,
                    status=406,
                    message=f'Сумма одного ордера меньше минимальной допустимой суммы (10 USDT)'
                )

            orders = []
            for symbol in symbols:
                symbol_info = await self.exchange.fetch_ticker(symbol)

                quantity = order_amount / symbol_info['ask']
                params = {'test': False}

                order = await self.exchange.create_market_buy_order(
                    symbol=symbol, amount=quantity, params=params
                )
                orders.append(order)

            return ExchangeResponse(
                result=orders,
                status=201,
                message='Ордер успешно создан'
            )

        except Exception as e:
            return ExchangeResponse(
                result=None,
                status=500,
                message=f'Ошибка при создании ордера: {e}'
            )