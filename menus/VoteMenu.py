from telebot import types


import sys
sys.path.append("..")



class VoteMenu(object):

    def __init__(self,variants):
        '''

        :param variants: should be list of typles (item,votes)
        '''
        self.markup = types.InlineKeyboardMarkup()
        self.markup.one_time_keyboard = True
        self.markup.add(types.InlineKeyboardButton("Закончить",callback_data="Vend"))
        for x,y in variants:
            self.markup.add(types.InlineKeyboardButton("{} {} руб. ({})".format(x.name,x.price,y),
                                                       callback_data="vote_{}".format(x.n)))



