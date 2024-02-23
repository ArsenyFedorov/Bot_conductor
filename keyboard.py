from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from text import *


class SimpleCallback(CallbackData, prefix="scb"):
    callback: str = " "
    day: int = 0
    time: str = " "


def kb_start():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=sign_up, callback_data="signUp")
    keyboard.button(text=schedule, callback_data="schedule")
    keyboard.button(text=setting, callback_data="setting")
    keyboard.adjust(1)
    return keyboard.as_markup()


def kb_sign_up_day():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=monday, callback_data=SimpleCallback(callback="day", day=0))
    keyboard.button(text=tuesday, callback_data=SimpleCallback(callback="day", day=1))
    keyboard.button(text=wednesday, callback_data=SimpleCallback(callback="day", day=2))
    keyboard.button(text=thursday, callback_data=SimpleCallback(callback="day", day=3))
    keyboard.button(text=friday, callback_data=SimpleCallback(callback="day", day=4))
    keyboard.button(text=saturday, callback_data=SimpleCallback(callback="day", day=5))
    keyboard.button(text=sunday, callback_data=SimpleCallback(callback="day", day=6))
    keyboard.button(text=major, callback_data="main")
    keyboard.adjust(2, 2, 2, 1)
    return keyboard.as_markup()


def kb_schedule():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=sign_up, callback_data="signUp")
    keyboard.button(text=major, callback_data="main")
    keyboard.adjust(1)
    return keyboard.as_markup()


def kb_clock(day_of_class: int = 0):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=morning, callback_data=SimpleCallback(callback="oclock", day=day_of_class, time="10"))
    keyboard.button(text=dinner, callback_data=SimpleCallback(callback="oclock", day=day_of_class, time="13"))
    keyboard.button(text=day, callback_data=SimpleCallback(callback="oclock", day=day_of_class, time="17"))
    keyboard.button(text=evening, callback_data=SimpleCallback(callback="oclock", day=day_of_class, time="20"))
    keyboard.button(text=major, callback_data="main")
    keyboard.adjust(2, 2)
    return keyboard.as_markup()


def kb_error():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=major, callback_data="main")


def kb_main():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=major, callback_data="main")
    return keyboard.as_markup()
