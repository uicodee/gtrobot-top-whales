import os
from dotenv import load_dotenv
import sys
import asyncio

from app.infrastructure.exchanges import ExchangeController


load_dotenv()

BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def binance_open_market_order_test():
    exchange_controller = ExchangeController(
        exchange_name='Binance', api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET
    )

    async with exchange_controller as exchange:
        result = await exchange.open_spot_market_orders(symbols=['BTC/USDT', 'ETH/USDT'], amount_usdt=10)
        print(result)


async def main():
    await binance_open_market_order_test()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
