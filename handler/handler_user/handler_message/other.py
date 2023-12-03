from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import F

import keyboard.reply
from data import DATA

router = Router()


@router.message()
async def digest(msg: Message):
    await msg.answer(f"Что-то пошло не так...")
