from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import Router, F
from src.bot.structures.text.text import info_text

info_more_router = Router(name='info_more_router')


@info_more_router.callback_query(F.data == 'info_more')
async def callback_info_more(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await callback.message.answer(text=info_text)
