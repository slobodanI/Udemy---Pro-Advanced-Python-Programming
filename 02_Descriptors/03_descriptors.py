# Creating Descriptors using Class

class Descriptors:

    def __init__(self, x=""):
        self.x = x

    def __get__(self, instance, owner):
        return f"{self.x} for {self.x}"

    def __set__(self, instance, value):
        if isinstance(value, str):
            self.x = value
        else:
            raise TypeError("X should always be a string")


class A(object):
    x = Descriptors()


y = A()
y.x = "John"
print(y.x)
