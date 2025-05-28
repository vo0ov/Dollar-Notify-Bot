import asyncio
import logging
import time

from aiogram import Bot

from api import get_usd_rate
from config import settings

logger = logging.getLogger(__name__)


async def send_start_rate_notify(bot: Bot, rate: float):
    """
    Отправляет уведомление владельцу о старте бота с текущим курсом USD.
    """

    msg = f'💵 Бот запущен. Текущий курс USD: <code><b>{rate:.2f}₽</b></code>'
    await bot.send_message(settings.owner_id, msg)
    logger.info(f'Уведомление о старте отправлено: {rate:.2f}₽')
    return rate


async def send_rate_notify(bot: Bot, old_rate: float, new_rate: float):
    """
    Отправляет уведомление владельцу о смене курса USD.
    """

    msg = f'💵 Курс USD изменился: <code><b>{old_rate:.2f}₽</b></code> → <code><b>{new_rate:.2f}₽</b></code>'
    await bot.send_message(settings.owner_id, msg)
    logger.info(f'Уведомление отправлено: {old_rate:.2f} -> {new_rate:.2f}')


async def run_notify_loop(bot: Bot):
    """
    Цикл: проверяет курс доллара с фиксированным интервалом.
    Если курс изменился — вызывает send_rate_notify().
    Если это первый запуск — вызывает send_start_rate_notify().
    """

    # Логируем запуск цикла и устанавливаем интервал проверки
    logger.info('Запуск цикла проверки курса USD...')
    interval = settings.check_interval
    next_run = time.monotonic()
    last_rate = None

    while True:
        next_run += interval

        try:
            # Получаем текущий курс USD
            rate = await get_usd_rate()

            # Если есть старый курс и курс изменился — шлём уведомление
            if last_rate is not None and rate != last_rate:
                await send_rate_notify(bot, last_rate, rate)

            elif last_rate is None:
                logger.info(f'Стартовый курс USD: {rate:.2f}₽')
                await send_start_rate_notify(bot, rate)

            else:
                logger.info(f'Курс USD не изменился: {rate:.2f}₽')

            last_rate = rate

        except Exception as e:
            logger.error(f'Ошибка в цикле проверки курса: {e}')

        # Ждём до следующего планового запуска
        await asyncio.sleep(max(0, next_run - time.monotonic()))
