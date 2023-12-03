from aiogram import Router
from aiogram import F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboard.callback import get_inline_kb
from data import DATA
from state import UserState

router = Router()


@router.callback_query(F.data == "start_test")
async def start_test(callback: CallbackQuery, state: FSMContext):
    await state.set_state(UserState.test)
    await state.update_data(q_num=0)
    text, answers = DATA.question[0]
    await callback.message.edit_text(text=text, reply_markup=get_inline_kb(answers))


@router.callback_query(StateFilter(UserState.test))
async def start_test(callback: CallbackQuery, state: FSMContext):
    data: dict = await state.get_data()
    user_answers = data.setdefault("user_answers", [])
    user_answers.append(int(callback.data))
    q_num = data["q_num"]
    q_num += 1
    await state.update_data(q_num=q_num, user_answers=user_answers)
    try:
        text, answers = DATA.question[q_num]
        await callback.message.edit_text(text=text, reply_markup=get_inline_kb(answers))
    except IndexError:
        await callback.message.edit_text(text=", ".join([str(i) for i in user_answers]))
