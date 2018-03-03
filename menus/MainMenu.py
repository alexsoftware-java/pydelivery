from telebot import types
from .__init__ import bot,r

import sys
sys.path.append("..")
from Classes.users import User


class MainMenu(object):

    def __init__(self):
        #User user(1)
        self.__variants = ['Сделать заказ','Мои заказы']
        self.markup = types.ReplyKeyboardMarkup()
        self.markup.one_time_keyboard = True
        for i in self.__variants:
            self.markup.row(types.KeyboardButton(i))





def getPhoto():
    return

