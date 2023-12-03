from aiogram import Router
from aiogram.types import Message
from aiogram import F

import keyboard.callback
from data import DATA

router = Router()


@router.message(F.text.lower().in_(["начать тест", "старт теста", "тест", "начать"]))
async def call_menu_test(msg: Message):
    await msg.answer(DATA.message.call_menu_test,
                     reply_markup=keyboard.callback.call_menu_test)
