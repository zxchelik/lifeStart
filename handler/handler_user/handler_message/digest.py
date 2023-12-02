from aiogram import Router
from aiogram.types import Message
from aiogram import F

import keyboard.reply
from data import DATA

router = Router()


@router.message(F.text.lower().in_(["дайджест", "digest"]))
async def digest(msg: Message):
    await msg.answer(DATA.message.digest, reply_markup=keyboard.reply.digest)
