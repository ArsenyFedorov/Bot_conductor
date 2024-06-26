from aiogram import Router, F, Bot, types
from aiogram.types import Message, CallbackQuery, InputFile, InputMediaPhoto
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from keyboard import *
from text import *
from data_base.user import User
from data_base.day_of_class import DayOfSport
import datetime
import asyncio

handlers_router = Router()


@handlers_router.message(Command("start"))
async def com_start(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://i.pinimg.com/550x/5e/e8/39/5ee839d9f00ad2d81ece2f1d5c30ae5e.jpg",
                         caption=greeting, reply_markup=kb_start())
    user = User(message)


@handlers_router.callback_query(F.data == "main")
async def com_start(callback: CallbackQuery, bot: Bot):
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media="https://abrakadabra.fun/uploads/posts/2021-12/1640194500_4-abrakadabra-fun-p-"
                  "dumayushchii-chelovechek-dlya-prezentatsii-4.jpg",
            caption=major_text
        ),
        reply_markup=kb_start())


@handlers_router.callback_query(F.data == "signUp")
async def sign_up(callback: CallbackQuery, bot: Bot):
    user = User(callback.from_user.id)
    if user.message_time == 0:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media="https://img.freepik.com/premium-vector/ringing-alarm-clock-with"
                      "-two-bells-illustration-cartoon-isolated-dinamic-image-green-and"
                      "-yellow-color-morning-alarm-clock_124848-425.jpg",
                caption=alternative_setting_text
            ),
            reply_markup=kb_setting())
    else:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media="https://imageru.ru/uploads/posts/2016-05/1464711563_imageru.ru"
                      "_business-men-psd.jpg",
                caption=sign_up_text
            ),
            reply_markup=kb_sign_up_day())


@handlers_router.callback_query(F.data == "schedule")
async def schedule(callback: CallbackQuery, bot: Bot):
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media="https://kpfu.ru/portal/docs/F1590481391/1422605698.jpg",
            caption=schedule_text
        ),
        reply_markup=kb_schedule())


@handlers_router.callback_query(F.data == "setting")
async def setting(callback: CallbackQuery, bot: Bot):
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media="https://img.freepik.com/premium-vector/ringing-alarm-clock-with"
                  "-two-bells-illustration-cartoon-isolated-dinamic-image-green-and"
                  "-yellow-color-morning-alarm-clock_124848-425.jpg",
            caption=setting_text
        ),
        reply_markup=kb_setting())


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "day"))
async def day_class(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    day_of_class = callback_data.day
    current_day = datetime.date.today().weekday()
    if day_of_class == current_day:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media="https://www.meme-arsenal.com/memes/7714d9b5d983a693b3822670cc67a024.jpg",
                caption=error
            ),
            reply_markup=kb_main())
    else:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media="https://img.freepik.com/premium-vector/ringing-alarm-clock-with"
                      "-two-bells-illustration-cartoon-isolated-dinamic-image-green-and"
                      "-yellow-color-morning-alarm-clock_124848-425.jpg",
                caption=day_time
            ),
            reply_markup=kb_oclock(day_of_class))


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "oclock"))
async def oclock(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    day_sport = DayOfSport(callback)
    flag = True
    day_now = datetime.date.today()
    while flag:
        if callback_data.day == day_now.weekday():
            day_sport.datetime = datetime.datetime(day_now.year, day_now.month, day_now.day,
                                                   int(callback_data.time))
            day_sport.save()
            flag = False
        else:
            day_now += datetime.timedelta(days=1)
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media="https://kartinki.pics/uploads/posts/2022-02/thumbs/1645072209_"
                  "2-kartinkin-net-p-kartinki-bez-fona-dlya-prezentatsii-2.jpg",
            caption=finish
        ),
        reply_markup=kb_main())
    flag = True
    user = User(callback.from_user.id)
    while flag:
        now = datetime.datetime.now()
        if now.weekday() == callback_data.day and now.hour == user.message_time:
            await bot.edit_message_media(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                media=InputMediaPhoto(
                    media="https://uprostim.com/wp-content/uploads/2021/05/image183-1278x720.jpg",
                    caption=message_text
                ),
                reply_markup=kb_status(day_sport.datetime))
            today = datetime.datetime.now()
            print(today)
            flag = False
        await asyncio.sleep(3_600)


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "setting"))
async def setting_oclock(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    user = User(callback.from_user.id)
    user.message_time = int(callback_data.time)
    user.save()
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media="https://kartinki.pics/uploads/posts/2022-02/thumbs/1645072209_"
                  "2-kartinkin-net-p-kartinki-bez-fona-dlya-prezentatsii-2.jpg",
            caption=finish
        ),
        reply_markup=kb_main())


@handlers_router.callback_query(SimpleCallback.filter(F.callback == "status"))
async def choice_status(callback: CallbackQuery, bot: Bot, callback_data: SimpleCallback):
    sport_day = DayOfSport(callback_data.day_now)
    if callback_data.status == "yes":
        sport_day.status = "Подтвержено"
    else:
        sport_day.status = "Отклонено"
    await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=InputMediaPhoto(
            media="https://kartinki.pics/uploads/posts/2022-02/thumbs/1645072209_"
                  "2-kartinkin-net-p-kartinki-bez-fona-dlya-prezentatsii-2.jpg",
            caption=finish
        ),
        reply_markup=kb_main())
