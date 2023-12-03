# Главное меню, вызывается на старт ил меню. Также можно перейти в него из
# меню "Начать тест" по inline кнопке НАЗАД,
# Есть аналогичная кнопка в message.


from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import F

import keyboard.callback
import keyboard.reply
from data import DATA

router = Router()


@router.callback_query(F.data == 'menu')
async def menu_callback(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(DATA.message.menu, reply_markup=keyboard.reply.menu)
