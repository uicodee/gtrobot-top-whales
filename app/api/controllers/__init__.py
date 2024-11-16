from fastapi import FastAPI
from .whale import router as whale_router


def setup(app: FastAPI) -> None:
    app.include_router(router=whale_router, tags=["Whale"])
