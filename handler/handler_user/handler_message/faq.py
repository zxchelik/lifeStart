from aiogram import Router
from aiogram.types import Message
from aiogram import F

from data import DATA

router = Router()


@router.message(F.text.lower().in_(["faq", "вопросы", "частые вопросы"]))
async def faq(msg: Message):
    await msg.answer(DATA.message.faq)
