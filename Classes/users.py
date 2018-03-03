from run import r
import pickle


class User:
    id = 0
    first_name = ""
    phone_number = ""
    cart_num = 0
    key = ""
    stage = "" # на каком этапе юзер
    step = 0  # на какую пиццу юзер смотрит сейчас

    def __init__(self, id):
        self.id = id

    def load(self):
        pickled_object = pickle.dumps(self)
        self.key = 'user' + str(self.id)
        r.set(self.key, pickled_object)

def unload(key):
    unpacked_object = pickle.loads(r.get(key))
    return unpacked_object
