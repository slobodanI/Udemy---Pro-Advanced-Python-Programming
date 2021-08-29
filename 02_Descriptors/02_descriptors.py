# Creating Descriptors using Property

class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print("Getting the name")
        return self._name

    def setName(self, name):
        print(f"Setting the name to '{name}'")
        self._name = name

    def delName(self):
        print("Deleting the name")
        del self._name

    name = property(getName, setName, delName)


person1 = Person("John")
print(person1.name)

person1.name = "Steve"

del person1.name
