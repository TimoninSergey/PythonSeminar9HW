from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn_start = KeyboardButton('/start')
btn_help = KeyboardButton('/help')
btn_rules = KeyboardButton('/rules')

kb_main_menu.add(btn_start, btn_help)