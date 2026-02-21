import aiohttp

from aiogram import Router, types

from config.config import CRYPTOBOT_TOKEN

router = Router()

PRICE_USD = 5

@router.callback_query(lambda c: c.data == "buy_vpn")
async def buy(call: types.CallbackQuery):
    async with aiohttp.ClientSession() as session:
        headers = {"Crypto-Pay-API-Token": CRYPTOBOT_TOKEN}
        data = {
            "asset": "USDT",
            "amount": PRICE_USD
        }
        async with session.post("https://pay.crypt.bot/api/createInvoice", headers=headers, json=data) as r:
            res = await r.json()
            url = res["result"]["pay_url"]

    await call.message.answer(f"💳 Оплати VPN:\n{url}")