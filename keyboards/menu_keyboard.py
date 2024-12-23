from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from keyboards.text import *


user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Привет!')]
    ],
    resize_keyboard=True
)


admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=btn_admins), KeyboardButton(text=about_users_bot)]
    ],
    resize_keyboard=True
)


main_admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=btn_admins), KeyboardButton(text=about_users_bot)]
    ],
    resize_keyboard=True
)