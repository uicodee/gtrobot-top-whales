from fastapi import APIRouter, status

router = APIRouter(prefix="/whale")


@router.get(
    path="/wallet-data",
    description="Get whale wallet data",
    status_code=status.HTTP_200_OK,
)
async def get_whale_wallet_data():
    ...


@router.get(
    path="/wallets",
    description="Get whale wallets",
    status_code=status.HTTP_200_OK,
)
async def get_whale_wallets():
    ...


@router.put(
    path="/set-wallet-follow",
    description="Set whale wallet follow status",
    status_code=status.HTTP_200_OK,
)
async def set_whale_wallet_follow():
    ...


@router.put(
    path="/set-wallet-name",
    description="Set whale wallet name",
    status_code=status.HTTP_200_OK,
)
async def set_whale_wallet_name():
    ...


@router.get(
    path="/networks",
    description="Get available whale networks",
    status_code=status.HTTP_200_OK,
)
async def get_whale_networks():
    ...


@router.get(
    path="/tags",
    description="Get whale tags",
    status_code=status.HTTP_200_OK,
)
async def get_whale_tags():
    ...


@router.get(
    path="/set-wallet",
    description="Set whale wallet data",
    status_code=status.HTTP_202_ACCEPTED,
)
async def set_whale_wallet():
    ...


@router.post(
    path="/copy-wallet",
    description="Copy whale wallet",
    status_code=status.HTTP_202_ACCEPTED,
)
async def copy_whale_wallet():
    ...


@router.get(
    path="/user-purchased-assets",
    description="Get user's purchased assets",
    status_code=status.HTTP_200_OK,
)
async def get_user_purchased_assets(initData: str):
    ...
