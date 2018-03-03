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



@bot.message_handler(regexp="^Сделать.*")
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button_left = types.InlineKeyboardButton(text="<-", callback_data="to_left")
    callback_button_ord = types.InlineKeyboardButton(text="Добавить в корзину", callback_data="create_order")
    callback_button_right = types.InlineKeyboardButton(text="->", callback_data="to_right")
    keyboard.add(callback_button_ord)
    keyboard.add(callback_button_left, callback_button_right)
    #bot.send_message(message.chat.id, "Выбери, что хочешь заказать: ", reply_markup=keyboard )
    bot.send_photo(message.chat.id,caption = "Выбери, что хочешь заказать: ", reply_markup=keyboard, photo='https://telegram.org/img/t_logo.png')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "to_right":
            User.step+=1
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")



def getPhoto():
    return

