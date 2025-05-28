from aiogram import Router, types
from aiogram.filters import Command, CommandStart

from api import get_usd_rate

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    """Приветствие, курс доллара и список команд."""

    rate = await get_usd_rate()
    text = (
        f'👋 Привет! Это бот уведомлений о курсе доллара.\n\n'
        f'💵 Текущий курс USD: <b>{rate:.2f}₽</b>\n\n'
        f'Доступные команды:\n'
        f'/course — узнать текущий курс\n'
        f'/help — помощь'
    )
    await message.answer(text)


@router.message(Command('help'))
async def cmd_help(message: types.Message):
    """Краткая справка по командам."""

    text = (
        'ℹ️ Бот уведомляет о изменении курса доллара (USD).\n\n'
        'Команды:\n'
        '/course — узнать текущий курс\n'
        '/help — помощь\n'
    )
    await message.answer(text)


@router.message(Command('course'))
async def cmd_course(message: types.Message):
    """Выводит актуальный курс доллара."""

    rate = await get_usd_rate()
    await message.answer(f'💵 1 USD = <b>{rate:.2f}₽</b>')
