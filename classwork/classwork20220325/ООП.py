from abc import ABC


class AbstractClass(ABC):
    pass


class C(AbstractClass):
    def __init__(self, some_data):
        self.some_data = some_data

    def __del__(self): # destructor
        pass

    @property
    def prop(self):
        return self.some_data

    @prop.setter
    def prop(self, data):
        self.some_data = data

    @prop.deleter
    def prop(self):
        self.some_data = 0
