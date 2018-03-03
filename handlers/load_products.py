from Classes.catalog import Item

#photo = open('/tmp/photo.png', 'rb')     tb.send_photo(chat_id, photo)

#загружаем все пиццы
item1 = Item()
item1.description = "Состав: соус \"Делюкс\", салями, балык, перец болгарский, шампиньоны, помидоры, маслины"
item1.price = 600
item1.n = 1
item1.picture = "../photos/deluxe.jpg"
item1.load({"meat":1,"mushrooms":1, "fish":0})



item2 = Item()
item2.description = "Состав: соус \"Делюкс\", куриное филе, ананасы, кукуруза"
item2.price = 550
item2.n = 2
item2.picture = "../photos/hawaii.jpg"
item2.load({"meat":1,"mushrooms":0, "fish":0})


item3 = Item()
item3.description = "Состав: томатный соус, говядина (фарш), ветчина, пикантная пепперони, лук красный, маслины, сладкий перец, шампиньоны и моцарелла"
item3.price = 700
item3.n = 3
item3.picture = "../photos/mex.jpg"
item3.load({"meat":1,"mushrooms":1, "fish":0})

item4 = Item()
item4.description = "Состав: шампиньоны маринованные, лук красный, балык, белый соус \"Делюкс\", маслины, зелень"
item4.price = 800
item4.n = 4
item4.picture = "../photos/mushroom.jpg"
item4.load({"meat":0,"mushrooms":1, "fish":0})

item5 = Item()
item5.description = "Состав: соус \"Делюкс\", помидоры, пеперони, перчики халапенью"
item5.price = 650
item5.n = 5
item5.picture = "../photos/pepperoni.jpg"
item5.load({"meat":1,"mushrooms":0, "fish":0})

item6 = Item()
item6.description = "Состав: острый соус \"Делюкс\", сервелат, ветчина, помидоры, болгарский перец"
item6.price = 600
item6.n = 6
item6.picture = "../photos/south.jpg"
item6.load({"meat":1,"mushrooms":0, "fish":0})

item7 = Item()
item7.description = "Состав: белый соус \"Делюкс\", сёмга, креветки, крабовые палочки, помидоры"
item7.price = 600
item7.n = 7
item7.picture = "../photos/fishka.jpg"
item7.load({"meat":0,"mushrooms":0, "fish":1})

item8 = Item()
item8.description = "Состав: соус \"Делюкс\", кальмары, мидии, осьминоги, крабовое мясо, помидоры, маслины"
item8.price = 680
item8.n = 8
item8.picture = "../photos/sea.jpg"
item8.load({"meat":0,"mushrooms":0, "fish":1})

print(item8.description)

