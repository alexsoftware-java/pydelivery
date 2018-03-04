from telebot import types

class FancyMenu(object):
    def __init__(self):
        self.markup = types.InlineKeyboardMarkup()
        callback_button_left = types.InlineKeyboardButton(text="<-", callback_data="to_left")
        callback_button_ord = types.InlineKeyboardButton(text="Добавить в корзину", callback_data="add_to_cart")
        callback_button_right = types.InlineKeyboardButton(text="->", callback_data="to_right")
        self.markup.add(callback_button_ord)
        self.markup.add(callback_button_left, callback_button_right)




