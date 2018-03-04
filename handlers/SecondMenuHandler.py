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


@bot.message_handler(regexp="^Сделать.*|^Вернуться.*")
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
                if len(str(call.message.message_id)) >0:
                    bot.delete_message(call.message.chat.id,call.message.message_id)
                item = unload("item" + str(user.step))
                bot.send_photo(call.message.chat.id, caption=item.name+"\n"+item.description, reply_markup=keyboard,
                               photo=item.picture)

                #bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="jiii",reply_markup=keyboard)
        elif call.data == "to_left":
            if user.id == call.message.chat.id:
                if user.step < 2: user.step = 8
                user.step -= 1
                r.set("p{}".format(call.message.chat.id), user.step)
                if len(str(call.message.message_id)) >0:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                item = unload("item" + str(user.step))
                bot.send_photo(call.message.chat.id, caption = item.description, reply_markup=keyboard,
                               photo = item.picture)
        elif call.data == "add_to_cart":
            if user.id == call.message.chat.id:
                cart = Cart(user.id)
                item = unload("item" + str(user.step))
                cart.itemsID.append(item)
                cart.load()
                cart_keyboard = types.ReplyKeyboardMarkup()
                cart_keyboard.add("Моя корзина(" + str(len(cart.itemsID)) + ")")
                #bot.answer_callback_query(call.message.chat.id, show_alert=True, text="Еда успешно добавлена в корзину!")
                bot.send_message(call.message.chat.id, "Еда успешно добавлена в корзину!", reply_markup = cart_keyboard)
                r.set("p{}".format(call.message.chat.id), user.step)
                if len(str(call.message.message_id)) >0:
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                item = unload("item" + str(user.step))
                bot.send_photo(call.message.chat.id, caption=item.description, reply_markup=keyboard,
                               photo=item.picture)

@bot.message_handler(regexp="^Мо.*")
def cart_show(message):
    #cart = Cart(message.chat.id)
    cart = unload("cart"+str(message.chat.id))
    if len(cart.itemsID)>0:
        print("chat_id" + str(message.chat.id))
        # bot.delete_message(message.chat.id, message.message_id)
        markup = types.ReplyKeyboardRemove(selective=False)

        cart.sum = 0
        cart.text = ""
        for i in range(len(cart.itemsID)):
            k = i + 1
            cart.text += str(k) + ". " + cart.itemsID[i].name + "  " + str(cart.itemsID[i].price) + "\n"
            cart.sum += cart.itemsID[i].price
        cart.text += "<b>Итого: </b>" + str(cart.sum)
        cart.load()
        bot.send_message(message.chat.id, "<b>В вашей корзине:</b> \n" + cart.text, reply_markup=markup,
                         parse_mode="HTML")

        markup = types.ReplyKeyboardMarkup()
        markup.add("Оформить заказ", "Очистить корзину")
        bot.send_message(message.chat.id, "<b>Оформляем заказ? </b> \n", reply_markup=markup, parse_mode="HTML")
    else:
        markup = types.ReplyKeyboardMarkup()
        markup.add("Вернуться к выбору пиццы")
        bot.send_message(message.chat.id, "<b>В твоих заказах ничего нет :(</b> \n", reply_markup=markup, parse_mode="HTML")



@bot.message_handler(regexp="^Очистить.*")
def cart_clean(message):
    cart = unload("cart"+str(message.chat.id))
    cart.clean()
    markup = types.ReplyKeyboardMarkup()
    markup.add("Вернуться к выбору пиццы")
    bot.send_message(message.chat.id, "<b>В твоей корзине пусто</b> \n", reply_markup=markup, parse_mode="HTML")

@bot.message_handler(regexp="^Оформить.*")
def create_order(message):
    markup = types.ReplyKeyboardMarkup()
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    button_contact = types.KeyboardButton(text = "Отправить контакт", request_contact=True)
    markup.add(button_geo, button_contact)
    bot.send_message(message.chat.id, "<b>Чтобы получить свою пиццу, отправь свое местоположение или введи адрес: </b> \n", reply_markup=markup, parse_mode="HTML")

@bot.message_handler(content_types=['location', 'contact'])
def handle_location(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add("Оплатить")
    bot.send_message(message.chat.id, "<b>Кошелек или жизнь</b> \n", reply_markup=markup, parse_mode="HTML")


    #print("{0}, {1}".format(message.location.latitude, message.location.longitude))

@bot.message_handler(regexp="^Оплатить.*")
def cart_clean(message):
    cart = unload("cart"+str(message.chat.id))
    cart.clean()
    markup = types.ReplyKeyboardMarkup()
    markup.add("Где мой заказ?")
    bot.send_message(message.chat.id, "<b>Твой заказ готовится на нашей куууууууухне</b> \n", reply_markup=markup, parse_mode="HTML")