from telebot import types
from .__init__ import bot,r
from menus.FancyMenu import FancyMenu
from menus.RateMenu import RateMenu
import pickle
from .StartHandler import start_handler
from random import randint
import sys
sys.path.append("..")
from Classes.users import User
from Classes.cart import Cart

empty_cart = types.ReplyKeyboardMarkup(resize_keyboard=True)
empty_cart.add("Моя корзина (0)")
# вырузить из redis по ключу
def unload(key):
    print(key)
    unpacked_object = pickle.loads(r.get(key))
    return unpacked_object


@bot.message_handler(regexp="^Сделать.*|^Вернуться.*")
def any_msg(message):
    if r.get("Vpaying_{}".format(message.chat.id))is not None: return cart_show(message)
    user = User(message.chat.id)
    cart = Cart(user.id)
    cart.load()
    cart_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cart_keyboard.add("Моя корзина(" + str(len(cart.itemsID)) + ")")
    item=unload("item"+str(user.step))       #получили итем из базы по id
    keyboard = FancyMenu().markup
    bot.send_message(message.chat.id,"приступаем к выбору \n \n \n",reply_markup=cart_keyboard)
    bot.send_photo(message.chat.id,caption = item.description, reply_markup=keyboard, photo=item.picture)


    #bot.edit_message_reply_markup()

@bot.callback_query_handler(func=lambda call: True if "to" in call.data else False)
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
                cart_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
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
    if r.get("Vpaying_{}".format(message.chat.id)) is not None:
        print(int(r.get("Vpaying_{}".format(message.chat.id))))
        grp = True
        cart = unload("cart{}".format(int(r.get("Vpaying_{}".format(message.chat.id)))))
    else:
        cart = unload("cart"+str(message.chat.id))
        grp = False
    if len(cart.itemsID)>0:
        print("chat_id" + str(message.chat.id))
        # bot.delete_message(message.chat.id, message.message_id)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if grp:
            markup.add("Оформить заказ")
        else:
            markup.add("Оформить заказ", "Очистить корзину")
            markup.add("Вернуться к выбору пиццы")

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


        bot.send_message(message.chat.id, "<b>Оформляем заказ? </b> \n", reply_markup=markup, parse_mode="HTML")
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Вернуться к выбору пиццы")
        bot.send_message(message.chat.id, "<b>В твоих заказах ничего нет :(</b> \n", reply_markup=markup, parse_mode="HTML")


@bot.message_handler(regexp="^Очистить.*")
def cart_clean(message):
    cart = unload("cart"+str(message.chat.id))
    cart.clean()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Вернуться к выбору пиццы")
    bot.send_message(message.chat.id, "<b>В твоей корзине пусто</b> \n", reply_markup=markup, parse_mode="HTML")


@bot.message_handler(regexp="^Оформить.*")
def create_order(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    markup.add(button_geo)
    bot.send_message(message.chat.id, "<b>Чтобы получить свою пиццу, отправь свое местоположение </b> \n", reply_markup=markup, parse_mode="HTML")


@bot.message_handler(content_types=['location', 'contact'])
def handle_location(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.content_type is not 'contact':
        markup.add(types.KeyboardButton(text="Отправить контакт",request_contact=True))
        bot.send_message(message.chat.id, "<b>На всякий случай, нам также понадобится твой контакт"
                                          "на в</b> \n", reply_markup=markup, parse_mode="HTML")
    else:
        markup.add("Оплатить")
        bot.send_message(message.chat.id, "<b>Оплатите заказ</b> \n", reply_markup=markup, parse_mode="HTML")


    #print("{0}, {1}".format(message.location.latitude, message.location.longitude))

@bot.message_handler(regexp="^Оплатить.*")
def cart_clean(message):
    cart = unload("cart"+str(message.chat.id))
    cart.clean()
    if r.get("Vpaying_{}".format(message.chat.id)) is not None:
        r.delete("Vpaying_{}".format(message.chat.id))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Где мой заказ?")
    markup.add("Заказ приехал, оценить")
    markup.add("В главное меню")
    bot.send_message(message.chat.id, "<b>Твой заказ готовится</b> \n"
                                      "Мы напишем тебе чуть позже если понадобится уточнения адреса",
                     reply_markup=markup, parse_mode="HTML")


@bot.message_handler(regexp="меню")
def to_menu_handler(m):
    start_handler(m)


@bot.message_handler(regexp="^Где.*")
def where_is_it_handler(m):
    bot.send_location(m.chat.id,latitude=float("59.{}".format(randint(9000,9999))),
                      longitude=float("30.{}".format(randint(3000,4000))))


@bot.message_handler(regexp="оценить")
def gimme_five_handler(m):
    menu = RateMenu().markup
    bot.send_message(m.chat.id,"оцените нас",reply_markup=menu)


@bot.message_handler(regexp="👍|😐|👎|😡")
def what_wrong_handler(m):
    bot.send_message(m.chat.id,"Спасибо за отзыв")
    start_handler(m)

