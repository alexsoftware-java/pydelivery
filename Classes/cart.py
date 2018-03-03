from run import r
import pickle


class Cart:
    id = 0
    text = []  # strings array?
    itemsID = []
    price = 0
    discount = 0
    key = ""

    def load(self):
        pickled_object = pickle.dumps(self)
        self.key = 'cart'+str(self.id)
        r.set(self.key, pickled_object)

    def unload(self):
        unpacked_object = pickle.loads(r.get(self.key))
        return unpacked_object


