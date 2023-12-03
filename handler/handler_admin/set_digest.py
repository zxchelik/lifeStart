from aiogram import Router
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram import F

from keyboard.callback import admin
from data import DATA
from config import ADMINS

router = Router()


@router.callback_query(F.from_user.id.in_(ADMINS) and F.data=="set_digest")
async def set_digest(callback: CallbackQuery):
    pass
