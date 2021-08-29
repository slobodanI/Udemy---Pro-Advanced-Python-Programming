# Uses of Descriptors
# data and non-data descriptors

# import random
# import time
#
#
# class Lazy:
#     def __init__(self, function):
#         self.function = function
#         self.name = function.__name__
#
#     def __get__(self, instance, owner=None) -> object:
#         instance.__dict__[self.name] = self.function(instance)
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         pass
#
#
# class Waiting:
#
#     @Lazy
#     def wait(self):
#         time.sleep(3)
#         return 42
#
#
# x = Waiting()
# print(x.wait)
# print(x.wait)
# print(x.wait)

# -------------------------------------------------------------------
# DRY
# here it works:
# https://realpython.com/python-descriptors/#dry-code

class EvenNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner=None) -> object:
        return instance.__dict__.get(self.name) or 0

    def __set__(self, instance, value) -> None:
        instance.__dict__[self.name] = (value if value % 2 == 0 else 0)


class Values:
    value1 = EvenNumber()
    value2 = EvenNumber()
    value3 = EvenNumber()
    value4 = EvenNumber()
    value5 = EvenNumber()


my_values = Values()
my_values.value1 = 1
my_values.value2 = 4
print(my_values.value1)
print(my_values.value2)
