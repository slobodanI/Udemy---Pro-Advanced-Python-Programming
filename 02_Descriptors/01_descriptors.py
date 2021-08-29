# Purpose of Descriptors

# without descriptors
# class Person:
#     def __init__(self, name, age, bmi):
#         self.name = name
#         self.age = age
#         self.bmi = bmi
#         if isinstance(self.name, str):
#             print(self.name)
#         else:
#             raise ValueError("Name of the person can never be an integer")
#         if self.bmi < 0:
#             raise ValueError("Bmi can never be less than zero")
#
#     def __str__(self):
#         return "{0} age is {1} with a bmi of {2}".format(self.name, self.age, self.bmi)
#
#
# person1 = Person("John", "25", 17)
# print(person1)

class Descriptors:
    def __init__(self):
        self.__bmi = 0

    def __get__(self, instance, owner):
        return self.__bmi

    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)
        else:
            raise TypeError("Bmi can only be an integer")

        if value < 0:
            raise ValueError("Bmi can never be less than zero")

        self.__bmi = value

    def __delete__(self, instance):
        del self.__bmi


class Person:
    bmi = Descriptors()

    def __init__(self, name, age, bmi):
        self.name = name
        self.age = age
        self.bmi = bmi

    def __str__(self):
        return f"{self.name} age is {self.age} and his bmi is {self.bmi}"


person1 = Person("John", 25, 17)
print(person1)

person2 = Person("John", 25, 48)
print(person2)
