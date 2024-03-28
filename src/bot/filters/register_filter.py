from aiogram.filters import BaseFilter


class RegisterFilter(BaseFilter):
    async def __call__(self, *args, **kwargs):
        return True
