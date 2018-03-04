import telebot
from .__init__ import bot,r


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