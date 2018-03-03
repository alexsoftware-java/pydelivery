import telebot
from telebot import types
import time
import re
import urllib
import os
import os.path
import sys

TOKEN = open('token.txt', 'r').read()
print(TOKEN)


knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start': 'Get used to the bot',
    'help': 'Gives you information about the available commands',
    'downloadTorrent': 'Start downloading'
}

# only used for console output
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard
bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener

# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Hi and Welcome!", reply_markup=hideBoard)
        bot.send_message(cid, ("\n"
                               "\n"
                               "	I'm able to download torrents for you and send files via telegram\n"
                               "\n"
                               "	Also I can make video smaller to faster download\n"
                               "\n"
                               "	"))
    else:
        bot.send_message(cid, "Hi, I already know you!", reply_markup=hideBoard)
        bot.send_message(cid, """

        I'm able to download torrents for you and send files via telegram

        Also I can make video smaller to faster download

        """)

bot.polling()