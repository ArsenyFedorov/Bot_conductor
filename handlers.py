from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.filters import Command
from keyboard import *
from text import *
import emoji

handlers_router = Router()


@handlers_router.message(Command("start"))
async def com_start(message: Message, bot: Bot):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://i.pinimg.com/550x/5e/e8/39/5ee839d9f00ad2d81ece2f1d5c30ae5e.jpg",
                         caption=greeting, reply_markup=kb_start())


@handlers_router.callback_query(F.data == "main")
async def com_start(callback: CallbackQuery, bot: Bot):
    await bot.delete_message(chat_id=callback.message.chat.id,
                             message_id=callback.message.message_id)
    await bot.send_photo(chat_id=callback.from_user.id,
                         photo="https://abrakadabra.fun/uploads/posts/2021-12/1640194500_4-abrakadabra-fun-p-"
                               "dumayushchii-chelovechek-dlya-prezentatsii-4.jpg",
                         caption=major_text, reply_markup=kb_start())


@handlers_router.callback_query(F.data == "signUp")
async def sign_up(callback: CallbackQuery, bot: Bot):
    await bot.delete_message(chat_id=callback.message.chat.id,
                             message_id=callback.message.message_id)
    await bot.send_photo(callback.from_user.id,
                         photo="https://imageru.ru/uploads/posts/2016-05/1464711563_imageru.ru"
                               "_business-men-psd.jpg",
                         caption=sign_up_text, reply_markup=kb_sign_up_day())


@handlers_router.callback_query(F.data == "schedule")
async def schedule(callback: CallbackQuery, bot: Bot):
    await bot.delete_message(chat_id=callback.message.chat.id,
                             message_id=callback.message.message_id)
    await bot.send_photo(callback.from_user.id, photo="https://kpfu.ru/portal/docs/F1590481391/1422605698.jpg",
                         caption=schedule_text, reply_markup=kb_schedule())


@handlers_router.callback_query(F.data == "setting")
async def setting(callback: CallbackQuery, bot: Bot):
    await bot.delete_message(chat_id=callback.message.chat.id,
                             message_id=callback.message.message_id)
    await bot.send_photo(callback.from_user.id,
                         photo="https://img.freepik.com/premium-vector/ringing-alarm-clock-with"
                               "-two-bells-illustration-cartoon-isolated-dinamic-image-green-and"
                               "-yellow-color-morning-alarm-clock_124848-425.jpg",
                         caption=setting_text, reply_markup=kb_setting())


@handlers_router.callback_query(F.data == "day")
async def day_class(callback: CallbackQuery, bot: Bot):
    await bot.delete_message(chat_id=callback.message.chat.id,
                             message_id=callback.message.message_id)
    await bot.send_message(callback.from_user.id, text="ARBUZIKI")


@handlers_router.callback_query(F.data == "oclock")
async def oclock(callback: CallbackQuery, bot: Bot):
    await bot.delete_message(chat_id=callback.message.chat.id,
                             message_id=callback.message.message_id)
    await bot.send_message(callback.from_user.id, text="BANANCHIKI")
