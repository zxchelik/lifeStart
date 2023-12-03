from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

call_menu_test = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text="да", callback_data="start_test")],
    [InlineKeyboardButton(text="назад", callback_data="menu")]
], resize_keyboard=True)

