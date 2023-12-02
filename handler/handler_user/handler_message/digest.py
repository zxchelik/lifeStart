from aiogram import Router
from aiogram.types import Message
from aiogram import F

from data import DATA

router = Router()


@router.message(F.text.lower().in_(["дайджест", "digest"]))
async def digest(msg: Message):
    await msg.answer(DATA.message.digest)
