from telebot import types


import sys
sys.path.append("..")



class MainMenu(object):

    def __init__(self,variants):
        '''

        :param variants: should be list of typles (item,votest)
        '''
        self.markup = types.ReplyKeyboardMarkup()
        self.markup.one_time_keyboard = True
        for x,y in variants:
            self.markup.add(types.InlineKeyboardButton("{} ({})".format(x.name,y)))

