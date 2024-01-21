from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboard import *
from text import *

handlers_router = Router()


@handlers_router.message(Command("start"))
async def com_start(message: Message):
    await message.answer(text=greeting, reply_markup=kb_start())


@handlers_router.callback_query(F.data == "signUp")
async def com_start(callback: CallbackQuery, bot: Bot):
    await bot.send_message(callback.from_user.id, text=sign_up_text, reply_markup=kb_sign_up_day())


@handlers_router.callback_query(F.data == "schedule")
async def com_start(callback: CallbackQuery, bot: Bot):
    await bot.send_message(callback.from_user.id, text=schedule_text, reply_markup=kb_schedule())


@handlers_router.callback_query(F.data == "day")
async def day_class(callback: CallbackQuery, bot: Bot):
    await bot.send_message(callback.from_user.id, text="ARBUZIKI")
