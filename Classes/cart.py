from run import r
import pickle


class Cart(object):
    id = 0
    itemsID = []
    sum = 0
    key = ""
    text = ""

    def __init__(self, id):
        self.id = id

    def load(self):
        pickled_object = pickle.dumps(self)
        self.key = 'cart'+str(self.id)
        r.set(self.key, pickled_object)

    def clean(self):
        self.itemsID.clear()
        self.load()

def unload(key):
    unpacked_object = pickle.loads(r.get(key))
    return unpacked_object
