import telebot
from .__init__ import bot,r


@bot.message_handler(commands=["pizza_vote"])
def VoteHandler(m):
    cid = m.chat.id
