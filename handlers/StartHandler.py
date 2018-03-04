import telebot
from .__init__ import bot,r,MainMenu


@bot.message_handler(commands=['start'])
def start_handler(m):
    cid = m.chat.id
    bot.send_message(cid,"Привет {}! Добро пожаловать \n"
                     "Я - бот от комманды тележка еды \n"
                     "Используй меня чтобы заказать пиццу".format(m.chat.first_name),
                     reply_markup=MainMenu().markup)


@bot.edited_message_handler(content_types=["location"])
def test_loc_hadnler(m):
    cid = r.get("LIVE_CID")
    mid = r.get("LIVE_MID")
    if cid is m.chat.id: return
    lat = m.location.latitude
    lon = m.location.longitude
    print(m.location,m.chat.id)
    try:
        bot.edit_message_live_location(lat,lon,cid,mid)
    except: pass