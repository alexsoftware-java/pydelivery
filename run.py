import telebot
from telebot import types
# from handlers import *
from listner import listener
import redis

r = redis.StrictRedis(host="10.20.3.190",db=0)

with open("token.txt",'r') as f: TOKEN = f.readline()

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)
try:
    from handlers import *
except:
    pass

bot.polling()

