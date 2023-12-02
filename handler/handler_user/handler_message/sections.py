# Главное меню, вызывается на старт ил меню. Также можно перейти в него из
# Дайджеста по reply кнопке ВЕРНУТЬСЯ В ГЛАВ МЕНЮ,
# Ответы и результат(после завершения теста) по reply кнопке ВЕРНУТЬСЯ В ГЛАВ МЕНЮ.
# Есть аналогичная кнопка в callback.

from aiogram import Router
from aiogram.types import Message
from aiogram import F

import keyboard.reply
from data import DATA

router = Router()


@router.message(F.text.lower().in_(["секции"]))
async def sections(msg: Message):
    await msg.answer(DATA.message.sections, reply_markup=keyboard.reply.sections)
