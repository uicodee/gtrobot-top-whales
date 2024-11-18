import os
from dotenv import load_dotenv
import sys
import asyncio

from app.infrastructure.exchanges import ExchangeController


load_dotenv()

BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')

BYBIT_API_KEY = os.getenv('BYBIT_API_KEY')
BYBIT_API_SECRET = os.getenv('BYBIT_API_SECRET')

MEXC_API_KEY = os.getenv('MEXC_API_KEY')
MEXC_API_SECRET = os.getenv('MEXC_API_SECRET')

BITGET_API_KEY = os.getenv('BITGET_API_KEY')
BITGET_API_SECRET = os.getenv('BITGET_API_SECRET')
BITGET_API_PASSPHRASE = os.getenv('BITGET_API_PASSPHRASE')

OKX_API_KEY = os.getenv('OKX_API_KEY')
OKX_API_SECRET = os.getenv('OKX_API_SECRET')
OKX_API_PASSPHRASE = os.getenv('OKX_API_PASSPHRASE')


if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def binance_open_market_order_test():
    exchange_controller = ExchangeController(
        exchange_name='Binance', api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET
    )

    async with exchange_controller as exchange:
        result = await exchange.open_spot_market_orders(symbols=['BTC/USDT'], amount_usdt=10)
        print(result)


async def bybit_open_market_order_test():
    exchange_controller = ExchangeController(
        exchange_name='Bybit', api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET
    )

    async with exchange_controller as exchange:
        result = await exchange.open_spot_market_orders(symbols=['BTC/USDT'], amount_usdt=10)
        print(result)


async def mexc_open_market_order_test():
    exchange_controller = ExchangeController(
        exchange_name='Mexc', api_key=MEXC_API_KEY, api_secret=MEXC_API_SECRET
    )

    async with exchange_controller as exchange:
        result = await exchange.open_spot_market_orders(symbols=['METAL/USDT'], amount_usdt=10)
        print(result)


async def bitget_open_market_order_test():
    exchange_controller = ExchangeController(
        exchange_name='Bitget', api_key=BITGET_API_KEY, api_secret=BITGET_API_SECRET, api_passphrase=BITGET_API_PASSPHRASE
    )

    async with exchange_controller as exchange:
        result = await exchange.open_spot_market_orders(symbols=['BTC/USDT'], amount_usdt=10)
        print(result)


async def okx_open_market_order_test():
    exchange_controller = ExchangeController(
        exchange_name='Okx', api_key=OKX_API_KEY, api_secret=OKX_API_SECRET, api_passphrase=OKX_API_PASSPHRASE
    )

    async with exchange_controller as exchange:
        result = await exchange.open_spot_market_orders(symbols=['BTC/USDT'], amount_usdt=10)
        print(result)


async def main():
    await binance_open_market_order_test()
    # await bybit_open_market_order_test()
    # await mexc_open_market_order_test()
    # await bitget_open_market_order_test()
    # await okx_open_market_order_test()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
