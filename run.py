import redis
import telebot

from listner import listener

r = redis.StrictRedis(host="10.20.3.190",db=0)

with open("token.txt",'r') as f: TOKEN = f.readline()

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)
try:
    from handlers import *
except:
    pass
bot.polling()

