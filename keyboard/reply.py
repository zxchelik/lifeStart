from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Дайджест")],
    [KeyboardButton(text="FAQ")],
    [KeyboardButton(text="Секции")],
    [KeyboardButton(text="Тест")]
], resize_keyboard=True)

sections = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Корпус 1")],
    [KeyboardButton(text="Корпус 2")],
    [KeyboardButton(text="Корпус 3")],
    [KeyboardButton(text="Назад в меню")]
], resize_keyboard=True)
