from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💳 Купить VPN", callback_data="buy_vpn")],
    [InlineKeyboardButton(text="📞 Поддержка", callback_data="support")]
])