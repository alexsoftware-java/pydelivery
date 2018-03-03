import telebot
from telebot import types
# from handlers import *
from listner import listener

with open("token.txt",'r') as f: TOKEN = f.readline()

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)
try:
    from handlers import *
except:
    pass

if __name__ == '__main__':
    bot.polling()

