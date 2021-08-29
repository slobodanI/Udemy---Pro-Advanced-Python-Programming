# Creating Descriptors using @Property

class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Getting the name")
        return self._name

    @name.setter
    def name(self, name):
        print("Setting the name")
        self._name = name

    @name.deleter
    def name(self):
        print("Deleting the name")
        del self._name


x = Person("Jim")
print(x.name)

x.name = "Mike"
del x.name
