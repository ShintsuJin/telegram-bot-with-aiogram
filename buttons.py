from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


b1 = KeyboardButton('/start')
b2 = KeyboardButton('/duty')

kb_client1 = ReplyKeyboardMarkup()


kb_client1.add(b1).add(b2)

