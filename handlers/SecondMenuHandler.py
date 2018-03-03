from telebot import types
from .__init__ import bot,r
from menus.FancyMenu import FancyMenu
import pickle

import sys
sys.path.append("..")
from Classes.users import User
from Classes.cart import Cart


# вырузить из redis по ключу
def unload(key):
    unpacked_object = pickle.loads(r.get(key))
    return unpacked_object


@bot.message_handler(regexp="^Сделать.*")
def any_msg(message):
    # global user
    user = User(message.chat.id)
    item=unload("item"+str(user.step))       #получили итем из базы по id
    keyboard = FancyMenu().markup
    #bot.send_message(message.chat.id, "Выбери, что хочешь заказать: ", reply_markup=keyboard )
    bot.send_photo(message.chat.id,caption = item.description, reply_markup=keyboard, photo=item.picture)




    #bot.edit_message_reply_markup()

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message and "to" in call.data:
        keyboard = FancyMenu().markup
        if not r.get("p{}".format(call.message.chat.id)): r.set("p{}".format(call.message.chat.id),0)
        user = User(call.message.chat.id)
        user.step = int(r.get("p{}".format(call.message.chat.id)))
        if call.data == "to_right":
            if user.id == call.message.chat.id:
                if user.step >7: user.step = 0
                user.step+=1
                r.set("p{}".format(call.message.chat.id), user.step)
                bot.delete_message(call.message.chat.id,call.message.message_id)
                item = unload("item" + str(user.step))
                bot.send_photo(call.message.chat.id, caption=item.description, reply_markup=keyboard,
                               photo=item.picture)

                #bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="jiii",reply_markup=keyboard)
        elif call.data == "to_left":
            if user.id == call.message.chat.id:
                if user.step < 2: user.step = 8
                user.step -= 1
                r.set("p{}".format(call.message.chat.id), user.step)
                bot.delete_message(call.message.chat.id, call.message.message_id)
                item = unload("item" + str(user.step))
                bot.send_photo(call.message.chat.id, caption=item.description, reply_markup=keyboard,
                               photo=item.picture)
        elif call.data == "add_to_cart":
            if user.id == call.message.chat.id:
                cart = Cart(user.id)
                item = unload("item"+str(user.step))
                cart.itemsID.append(item)
                cart.load()
                cart_keyboard = types.ReplyKeyboardMarkup()
                cart_keyboard.add("Моя корзина(" + str(len(cart.itemsID)) + ")")
                bot.send_message(call.message.chat.id, "Еда успешно добавлена в корзину!", reply_markup = cart_keyboard)
                r.set("p{}".format(call.message.chat.id), user.step)
                bot.delete_message(call.message.chat.id, call.message.message_id)
                item = unload("item" + str(user.step))
                bot.send_photo(call.message.chat.id, caption=item.description, reply_markup=keyboard,
                               photo=item.picture)

@bot.message_handler(regexp="^Моя.*")
def cart_show(message):
    #cart = Cart(message.chat.id)
    cart = unload("cart"+str(message.chat.id))
    #bot.delete_message(message.chat.id, message.message_id)
    markup = types.ReplyKeyboardRemove(selective=False)

    for i in range(len(cart.itemsID)):
        cart.text+=str(i+1)+". "+ cart.itemsID[i].name+"  "+str(cart.itemsID[i].price)+"\n"
    bot.send_message(message.chat.id, "<b>В вашей корзине:</b> \n"+cart.text, reply_markup=markup, parse_mode="HTML")
    in_cart_keyboard = types.InlineKeyboardMarkup()
    callback_button_left = types.InlineKeyboardButton(text="<-", callback_data="to_left")