# Главное меню, вызывается на старт ил меню. Также можно перейти в него из
# меню "Начать тест" по inline кнопке НАЗАД,
# Есть аналогичная кнопка в message.


from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.fsm import state

import keyboard.callback
from data import DATA

router = Router()

# ДОПИЛИТЬ
# нужно чтобы отвечала на menu из keyboard.callback.call_menu_test.
# поставить стейт test.
@router.callback_query()
async def menu_callback(callback: CallbackQuery):
    pass
