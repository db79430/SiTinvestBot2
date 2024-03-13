from aiogram import Router
from .invest_handlers import invest_router as invest_router


handlers_router = Router(name=__name__)

handlers_router.include_router(invest_router)
