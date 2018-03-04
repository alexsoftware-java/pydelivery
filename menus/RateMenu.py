from telebot import types


import sys
sys.path.append("..")



class RateMenu(object):

    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.markup.one_time_keyboard = True
        self.markup.add("👍👍👍👍👍")
        self.markup.add("👍👍👍👍")
        self.markup.add("😐")
        self.markup.add("👎")
        self.markup.add("😡")

