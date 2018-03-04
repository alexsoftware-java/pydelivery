import telebot
from .__init__ import bot,r
from menus.VoteMenu import VoteMenu
import sys
import pickle
sys.path.append("..")
from Classes.users import User
from Classes.cart import Cart
from telebot import types


from .SecondMenuHandler import unload
@bot.message_handler(commands=["pizza_vote"])
def VoteHandler(m):
    cid = m.chat.id
    try:
        quant = m.text.split()[1]
    except IndexError:
        bot.reply_to(m,"Укажите колличество пиц \n например /pizza_vote 2")
        return
    if r.get("IS_VOTE_{}".format(cid)):
        bot.send_message(cid,"голосование уже идет")
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
        if not r.get("IS_VOTE_{}".format(call.message.chat.id)):bot.answer_callback_query(call.id)
        if r.get("vUSER_{}_{}_{}".format(call.from_user.id,call.message.chat.id,call.message.message_id)):
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


@bot.callback_query_handler(func=lambda call: True if "Vend" in call.data else False)
def endvote_callback(call):
    if call.message and "Vend" in call.data:
        if not r.get("IS_VOTE_{}".format(call.message.chat.id)):
            bot.answer_callback_query(call.id)
            return
        cid = call.message.chat.id
        results = sorted(pickle.loads(r.get("vote_{}_{}".format(call.message.chat.id,call.message.message_id))),
                         key=lambda x: x[1])[:int(r.get("Qvote_{}_{}".format(cid, call.message.message_id)))]
        results, indexes = zip(*results)
        r.delete("IS_VOTE_{}".format(call.message.chat.id))
        r.delete("vote_{}_{}".format(call.message.chat.id,call.message.message_id))
        r.delete("Qvote_{}_{}".format(cid, call.message.message_id))
        cart = Cart(call.message.chat.id)
        print(cart.id)
        for item in results: cart.itemsID.append(item)
        cart.load()
        menu = types.InlineKeyboardMarkup()
        menu.one_time_keyboard = True
        menu.add(types.InlineKeyboardButton("оплатить",callback_data="Vpay"))
        menu.add(types.InlineKeyboardButton("отменить",callback_data="Vcancel"))
        bot.send_message(cid,"Голосование окончено",reply_markup=menu)


@bot.callback_query_handler(func=lambda call: True if "Vcancel" in call.data else False)
def cancel_callback(call):
    bot.send_message(call.message.chat.id,"Голосование отменено")


@bot.callback_query_handler(func=lambda call: True if "Vpay" in call.data else False)
def vote_pay_callback(call):
    r.set("Vpaying_{}".format(call.from_user.id),call.message.chat.id)
    bot.send_message(call.message.chat.id,"{} пожалуйста проследуйте"
                                          "в приватную переписку с ботом для "
                                          "подтверждения \n"
                                          "Перенаправление из главного меню".format(call.from_user.first_name))