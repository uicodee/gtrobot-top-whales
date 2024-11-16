from typing import Annotated

from aiogram.utils.web_app import check_webapp_signature, safe_parse_webapp_init_data
from fastapi import Request, HTTPException, status, Depends, Header

from app import dto
from app.api.dependencies.database import dao_provider
from app.config import Settings
from app.infrastructure.database import HolderDao


def get_telegram_user(
    authorization: Annotated[list[str] | None, Header(alias="Authorization")] = None
) -> dto.TelegramUser:
    raise NotImplementedError


class TelegramAuthProvider:

    def __init__(self, settings: Settings):
        self.settings = settings

    async def get_current_telegram_user(
        self, request: Request, dao: HolderDao = Depends(dao_provider)
    ) -> dto.TelegramUser:
        telegram_init_data = request.headers.get("Authorization")
        unauthorized_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
        bad_request_exception = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unregistered"
        )
        if telegram_init_data is None:
            raise unauthorized_exception
        if not check_webapp_signature(self.settings.tgbot.token, telegram_init_data):
            raise unauthorized_exception
        try:
            web_app_init_data = safe_parse_webapp_init_data(
                token=self.settings.tgbot.token, init_data=telegram_init_data
            )
        except:
            raise unauthorized_exception
        # Проверка пользователя на наличие
