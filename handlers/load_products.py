from Classes.catalog import Item

#photo = open('/tmp/photo.png', 'rb')     tb.send_photo(chat_id, photo)

#загружаем все пиццы

'''
<a href="https://ibb.co/eb3tf7"><img src="https://preview.ibb.co/gYW1YS/deluxe.jpg" alt="deluxe" border="0"></a>
<a href="https://ibb.co/hfTgYS"><img src="https://preview.ibb.co/f8s8DS/fishka.jpg" alt="fishka" border="0"></a>
<a href="https://ibb.co/cDitf7"><img src="https://preview.ibb.co/bKh8DS/hawaii.jpg" alt="hawaii" border="0"></a>
<a href="https://ibb.co/c6XVSn"><img src="https://preview.ibb.co/hWcx7n/mex.jpg" alt="mex" border="0"></a>
<a href="https://ibb.co/cdzYf7"><img src="https://preview.ibb.co/c9rPnn/mushroom.jpg" alt="mushroom" border="0"></a>
<a href="https://ibb.co/fzhfSn"><img src="https://preview.ibb.co/dJO9L7/pepperoni.jpg" alt="pepperoni" border="0"></a>
<a href="https://ibb.co/b9XfSn"><img src="https://preview.ibb.co/fdsfSn/sea.jpg" alt="sea" border="0"></a>
<a href="https://ibb.co/djR77n"><img src="https://preview.ibb.co/i1ob07/south.jpg" alt="south" border="0"></a>
<a href="https://ibb.co/dJTn7n"><img src="https://preview.ibb.co/ioWUL7/vegetarian.jpg" alt="vegetarian" border="0"></a>
'''


item1 = Item()
item1.name = "Веселый болгарин"
item1.description = "Состав: соус \"Делюкс\", салями, балык, перец болгарский, шампиньоны, помидоры, маслины"
item1.price = 600
item1.n = 1
item1.picture = "https://preview.ibb.co/gYW1YS/deluxe.jpg"
item1.load({"meat":1,"mushrooms":1, "fish":0})



item2 = Item()
item2.name = "Бодрый петух"
item2.description = "Состав: соус \"Особый\", куриное филе, ананасы, кукуруза"
item2.price = 550
item2.n = 2
item2.picture = "https://preview.ibb.co/f8s8DS/fishka.jpg"
item2.load({"meat":1,"mushrooms":0, "fish":0})


item3 = Item()
item3.name = "Все вместе"
item3.description = "Состав: томатный соус, говядина (фарш), ветчина, пикантная пепперони, лук красный, маслины, сладкий перец, шампиньоны и моцарелла"
item3.price = 700
item3.n = 3
item3.picture = "https://preview.ibb.co/hWcx7n/mex.jpg"
item3.load({"meat":1,"mushrooms":1, "fish":0})

item4 = Item()
item4.name = "Масляков"
item4.description = "Состав: шампиньоны маринованные, лук красный, балык, белый соус \"Делюкс\", маслины, зелень"
item4.price = 800
item4.n = 4
item4.picture = "https://preview.ibb.co/c9rPnn/mushroom.jpg"
item4.load({"meat":0,"mushrooms":1, "fish":0})

item5 = Item()
item5.name = "Простяковская"
item5.description = "Состав: соус, помидоры, пеперони, перчики халапенью"
item5.price = 650
item5.n = 5
item5.picture = "https://preview.ibb.co/dJO9L7/pepperoni.jpg"
item5.load({"meat":1,"mushrooms":0, "fish":0})

item6 = Item()
item6.name = "Мясокомбинат"
item6.description = "Состав: острый соус \"Делюкс\", сервелат, ветчина, помидоры, болгарский перец"
item6.price = 600
item6.n = 6
item6.picture = "https://preview.ibb.co/i1ob07/south.jpg"
item6.load({"meat":1,"mushrooms":0, "fish":0})

item7 = Item()
item7.name = "Океанариум"
item7.description = "Состав: белый соус \"Шеф\", сёмга, креветки, крабовые палочки, помидоры"
item7.price = 600
item7.n = 7
item7.picture = "https://preview.ibb.co/ioWUL7/vegetarian.jpg"
item7.load({"meat":0,"mushrooms":0, "fish":1})

item8 = Item()
item8.name = "Морское дно"
item8.description = "Состав: соус \"Блаженство\", кальмары, мидии, осьминоги, крабовое мясо, помидоры, маслины"
item8.price = 680
item8.n = 8
item8.picture = "https://preview.ibb.co/fdsfSn/sea.jpg"
item8.load({"meat":0,"mushrooms":0, "fish":1})

print(item8.description)

