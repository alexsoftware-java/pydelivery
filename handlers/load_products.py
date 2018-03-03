from .catalog import Item
#photo = open('/tmp/photo.png', 'rb')     tb.send_photo(chat_id, photo)

#загружаем все пиццы
item1 = Item()
item1.description = "Состав: соус \"Делюкс\", салями, балык, перец болгарский, шампиньоны, помидоры, маслины"
item1.price = 600
item1.n = 1
item1.picture = "../photos/deluxe.jpg"
item1.load({"meat":1,"mushrooms":1, "fish":0})

print(item1.description)

item2 = Item()
item2.description = "Состав: соус \"Делюкс\", куриное филе, ананасы, кукуруза"
item2.price = 550
item2.n = 2
item2.picture = "../photos/hawaii.jpg"
item2.load({"meat":1,"mushrooms":0, "fish":0})


item3 = Item()
item3.description = "Состав: соус \"Делюкс\", куриное филе, ананасы, кукуруза"
item3.price = 550
item3.n = 3
item3.picture = "../photos/mex.jpg"
item3.load({"meat":1,"mushrooms":0, "fish":0})
