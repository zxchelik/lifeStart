from aiogram import Router
from aiogram.types import Message
from aiogram import F

from data import DATA

from config import CHANNEl

router = Router()


# Для теста указал айди своего канал.
@router.channel_post(
    F.sender_chat.id == -1002082046843 and
    F.text.lower().contains('#дайджест'))  # TODO  айди заменить на CHANNEL.
async def channel_post(post: Message):
    pass
