from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Задание 1: Reply-клавиатура для /start
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет")],
        [KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True
)

# Задание 2: Inline-клавиатура с URL
links_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://news.google.com")],
        [InlineKeyboardButton(text="Музыка", url="https://music.youtube.com")],
        [InlineKeyboardButton(text="Видео", url="https://youtube.com")]
    ]
)

# Задание 3: Клавиатуры для динамического изменения
def get_dynamic_keyboard(show_more=False):
    if not show_more:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
            ]
        )
    else:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Опция 1", callback_data="option_1"),
                 InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
            ]
        )