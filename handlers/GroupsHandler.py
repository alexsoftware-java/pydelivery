import telebot
from .__init__ import bot,r
from menus.VoteMenu import VoteMenu
import sys
import pickle
sys.path.append("..")
from Classes.users import User
from .SecondMenuHandler import unload
@bot.message_handler(commands=["pizza_vote"])
def VoteHandler(m):
    cid = m.chat.id
    try:
        quant = m.text.split()[1]
    except IndexError:
        bot.reply_to(m,"Укажите колличество пиц \n например /pizza_vote 2")
        return
    items = tuple(zip([unload("item"+str(x)) for x in range(1,7)],
                [0 for x in range(1,7)]))
    menu = VoteMenu(items).markup
    mess = bot.send_message(cid,"Выбирайте!", reply_markup=menu)
    r.set("vote_{}_{}".format(cid,mess.message_id),pickle.dumps(items))
    r.set("Qvote_{}_{}".format(cid, mess.message_id), quant)
    r.set("IS_VOTE_{}".format(cid),1)

@bot.callback_query_handler(func=lambda call: True if "vote" in call.data else False)
def callback_vote(call):
    if call.message and "vote" in call.data:
        if r.get("vUSER_{}_{}_{}".format(call.from_user.id,call.message.chat.id,call.message.message_id)):
            print(call)
            bot.answer_callback_query(call.id)
        else:
            r.set("vUSER_{}_{}_{}".format(call.from_user.id,call.message.chat.id,call.message.message_id),1)
            items,scores = zip(*pickle.loads(r.get("vote_{}_{}".format(call.message.chat.id,call.message.message_id))))
            scores = list(scores)
            scores[int(call.data.strip("_")[-1])-1] +=1
            results = zip(items,scores)
            r.set("vote_{}_{}".format(call.message.chat.id,call.message.message_id),pickle.dumps(results))
            menu = VoteMenu(results).markup
            bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,
                                          call.inline_message_id,
                                          menu)