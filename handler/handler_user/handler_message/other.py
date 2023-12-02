from aiogram import Router
from aiogram.types import Message
from aiogram import F

import keyboard.reply
from data import DATA

router = Router()


@router.message()
async def digest(msg: Message):
    await msg.answer("Что-то пошло не так")
