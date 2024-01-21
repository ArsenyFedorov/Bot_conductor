from aiogram.utils.keyboard import InlineKeyboardBuilder
from text import *


def kb_start():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=sign_up, callback_data="signUp")
    keyboard.button(text=schedule, callback_data="schedule")
    keyboard.adjust(1)
    return keyboard.as_markup()


def kb_sign_up_day():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=monday, callback_data="day")
    keyboard.button(text=tuesday, callback_data="day")
    keyboard.button(text=wednesday, callback_data="day")
    keyboard.button(text=thursday, callback_data="day")
    keyboard.button(text=friday, callback_data="day")
    keyboard.button(text=saturday, callback_data="day")
    keyboard.button(text=sunday, callback_data="day")
    return keyboard.as_markup()


def kb_schedule():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=sign_up, callback_data="signUp")
    return keyboard.as_markup()
