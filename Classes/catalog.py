from run import r
import pickle

class Item:
    description = ''
    price = 0
    size = 0
    pastry = True
    picture = ''
    n = 0
    key = ''
    tags = {}

#загрузить в redis
    def load(self, tags):
        self.tags = tags
        pickled_object = pickle.dumps(self)
        print('one object was loaded')
        self.key = 'item'+str(self.n)
        r.hmset('hmset_'+self.key,tags)
        r.set(self.key, pickled_object)

# вырузить из redis по ключу
def unload(key):
    unpacked_object = pickle.loads(r.get(key))
    return unpacked_object


item = Item()
item.description = "Описание :)"
item.price = 1200
item.n = 0
item.picture = "a link"

print(item.description)

item.load({"meat":1,"mushrooms":0, "fish":0})

print("key: "+item.key)

my_object = unload('item0')

print("desc: "+my_object.description)
print(r.hmget("hmset_item0", "meat"))
print(r.hmget("hmset_item0", "mushrooms"))


