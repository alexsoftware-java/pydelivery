import telebot
from .__init__ import bot,r,MainMenu


@bot.message_handler(commands=['start'])
def start_handler(m):
    cid = m.chat.id
    bot.send_message(cid,"Привет {}! Добро пожаловать \n"
                     "Я - бот от комманды тележка еды \n"
                     "Используй меня чтобы заказать пиццу".format(m.chat.first_name),
                     reply_markup=MainMenu().markup)

