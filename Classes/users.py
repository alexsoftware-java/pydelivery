from run import bot,r
import pickle

class User:
    id = 0
    first_name = ""
    phone_number = ""
    cart_num = 0
    key = ""

    def load(self):
        pickled_object = pickle.dumps(self)
        self.key = 'user' + str(self.id)
        r.set(self.key, pickled_object)

    def unload(self):
        unpacked_object = pickle.loads(r.get(self.key))
        return unpacked_object
