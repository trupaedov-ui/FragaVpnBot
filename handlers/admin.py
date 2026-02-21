from aiogram import Router, types
from aiogram.filters import Command

from config.config import ADMIN_ID

router = Router()

@router.message(Command("admin"))
async def admin_handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer("👑 Админ панель скоро будет")