from telebot import types
from .__init__ import bot

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


# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    user_name = m.chat.first_name
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Привет и Добро пожаловать!", reply_markup=hideBoard)
 #      bot.send_message(cid, ("\n"
 #                              "\n"
 #                              "\n"
 #                              "\n"
 #                              "\n"
 #                              "	"))
    else:
        bot.send_message(cid, "Привет, "+user_name, reply_markup=hideBoard)
        bot.send_message(cid, """
            Ha
        """)