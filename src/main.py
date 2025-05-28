import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from config import settings
from handlers import router
from middlewares import OwnerOnlyMiddleware
from notify import run_notify_loop

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)

# Создаем логгер для текущего модуля
logger = logging.getLogger(__name__)


async def main():
    """
    Основная функция для запуска Telegram-бота.
    """

    # Создаем экземпляр бота с токеном из конфига
    bot = Bot(token=settings.bot_token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Создаем диспетчер событий (обработка сообщений и команд)
    dp = Dispatcher()

    # Добавляем middleware для обработки сообщений только от владельца бота
    dp.message.middleware(OwnerOnlyMiddleware())

    # Регистрируем все хендлеры (обработчики команд)
    dp.include_router(router)

    # Запускаем цикл уведомлений как отдельную асинхронную задачу
    asyncio.create_task(run_notify_loop(bot))

    # Сообщаем о запуске бота через логгер
    logger.info('Бот запущен. Нажмите Ctrl+C для остановки.')

    try:
        # Запуск polling-цикла — получение апдейтов от Telegram
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        # При отмене задачи (например, при Ctrl+C) — ничего не делаем
        pass

if __name__ == '__main__':
    try:
        # Запускаем асинхронную функцию main()
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # При остановке по Ctrl+C или завершении процесса — логируем событие
        logger.info('Бот остановлен.')
