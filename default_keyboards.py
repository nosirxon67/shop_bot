from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mahsulot sotish."),
            KeyboardButton(text="Mars mahsulotlari.")
        ],
        [
            KeyboardButton(text="Mening mahsulotlarm."),
            KeyboardButton(text="A'loqa.")
        ]
    ], resize_keyboard=True
)

