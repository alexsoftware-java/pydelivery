from telebot import types
from .__init__ import bot,r


class MainMenu(object):

    def __init__(self):
        self.__variants = ['Сделать заказ','мои заказы']
        self.markup = types.ReplyKeyboardMarkup()
        for i in self.__variants:
            self.markup.row(types.KeyboardButton(i))
