class WalletInfo:
    def __init__(self, wallet_id: int, user_id: int = 0, is_initial_data: bool = True):
        self.wallet_id = wallet_id
        self.user_id = user_id
        self.wallet_data = {}
        self.stocks = {}
        self.chart = []
        self.is_follow = False
        self.is_initial_data = is_initial_data

    async def get_wallet_data(self):
        ...

    async def get_stocks(self):
        ...

    async def get_chart(self):
        ...

    async def get_is_follow(self):
        ...

