from run import r
import pickle


class Cart(object):
    id = 0
    itemsID = []
    price = 0
    key = ""

    def __init__(self, id):
        self.id = id

    def load(self):
        pickled_object = pickle.dumps(self)
        self.key = 'cart'+str(self.id)
        r.set(self.key, pickled_object)

def unload(key):
    unpacked_object = pickle.loads(r.get(key))
    return unpacked_object
