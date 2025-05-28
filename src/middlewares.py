from aiogram import BaseMiddleware
from aiogram.types import Message

from config import settings


class OwnerOnlyMiddleware(BaseMiddleware):
    """
    Пропускает сообщения только от OWNER_ID, остальные игнорирует.
    """

    async def __call__(self, handler, event: Message, data):
        # Проверяем, если это не владелец — игнорируем (ничего не делаем)
        if getattr(event, 'from_user', None) and event.from_user.id != settings.owner_id:
            return  # Просто не вызываем handler

        # Если владелец — обрабатываем дальше
        return await handler(event, data)
