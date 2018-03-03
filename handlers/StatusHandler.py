import telebot
from .__init__ import bot,r


@bot.message_handler(commands=['status'])
def status_handler(m):
    # TODO: check for redis connection here
    cid = m.chat.id
    bot.send_message(cid,"online, Redis online: {}".format(r.ping()))


