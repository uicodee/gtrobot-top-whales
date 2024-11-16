from abc import ABC

from .base import BaseExchange


class BinanceExchange(BaseExchange, ABC):
    def __init__(self, api_key: str, api_secret: str, api_passphrase: str = None):
        super().__init__(api_key, api_secret, 'binance', api_passphrase)

    async def open_spot_market_orders(self, symbols: list[str], amount_usdt: float):
        try:
            exchange_balance = await self.get_free_balance('USDT')

            if exchange_balance < amount_usdt:
                return {
                    'result': None,
                    'status': 400,
                    'message': f'Недостаточно средств для открытия сделок: {exchange_balance} USDT'
                }

            orders = []
            order_amount = amount_usdt / len(symbols)

            if order_amount < 10:
                return {
                    'result': None,
                    'status': 400,
                    'message': f'Сумма 1 ордера меньше минимальной допустимой суммы (10 USDT)'
                }

            for symbol in symbols:
                self.exchange.options['defaultType'] = 'spot'
                symbol_info = await self.exchange.fetch_ticker(symbol)

                quantity = order_amount / symbol_info['ask']
                params = {'test': False}

                order = await self.exchange.create_market_buy_order(
                    symbol=symbol, amount=quantity, params=params
                )
                orders.append(order)

            return {
                'result': orders,
                'status': 200,
                'message': 'Ордер успешно создан'
            }

        except Exception as e:
            return {
                'result': None,
                'status': 500,
                'message': f'Ошибка при создании ордера: {e}'
            }
