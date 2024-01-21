from aiogram.utils.keyboard import InlineKeyboardBuilder
from text import *


def kb_start():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=sign_up, callback_data="signUp")
    keyboard.button(text=schedule, callback_data="schedule")
    keyboard.button(text=setting, callback_data="setting")
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
    keyboard.button(text=major, callback_data="main")
    keyboard.adjust(2, 2, 2, 1)
    return keyboard.as_markup()


def kb_schedule():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=sign_up, callback_data="signUp")
    keyboard.button(text=major, callback_data="main")
    keyboard.adjust(1)
    return keyboard.as_markup()


def kb_setting():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=morning, callback_data="oclock")
    keyboard.button(text=dinner, callback_data="oclock")
    keyboard.button(text=day, callback_data="oclock")
    keyboard.button(text=evening, callback_data="oclock")
    keyboard.button(text=major, callback_data="main")
    keyboard.adjust(2, 2)
    return keyboard.as_markup()
