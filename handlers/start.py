from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

# Создаём кнопку
buy_button = InlineKeyboardButton(text="💳 Купить VPN", callback_data="buy_vpn")

# Создаём клавиатуру сразу с кнопкой
main_menu = InlineKeyboardMarkup(inline_keyboard=[[buy_button]])

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "🚀 Fraga VPN Bot\n\nВыбери действие:",
        reply_markup=main_menu
    )