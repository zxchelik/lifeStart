from typing import Tuple

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import DATA

call_menu_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="да", callback_data="start_test")],
    [InlineKeyboardButton(text="назад", callback_data="menu")]
], resize_keyboard=True)


def get_inline_kb(buttons: list[Tuple]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for button in buttons:
        text, callback = button
        kb.add(InlineKeyboardButton(text=text, callback_data=callback))
    return kb.as_markup()



