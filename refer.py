from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


referat = KeyboardButton(text="referat")
referat1 = KeyboardButton(text="referat1")

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [referat, referat1]
    ],
    resize_keyboard=True
)


