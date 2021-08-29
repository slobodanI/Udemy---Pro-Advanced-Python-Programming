# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# new_dict_values = {k: v * 2 for (k, v) in my_dict.items()}
# print(new_dict_values)
# -----------------------------------

# my_dict = {i: i ** 2 for i in range(10) if i % 2 == 0}
# print(my_dict)
# -----------------------------------

# feh = {'temp1': 10, 'temp2': 20, 'temp3': 30, 'temp4': 40, }
#
# cel = list(map(lambda x: (float(5) / 9) * (x - 32), feh.values()))
# cel_dict = dict(zip(feh.keys(), cel))
# print(cel_dict)
# # same as...
# cel_dict = {k: (float(5) / 9) * (v - 32) for (k, v) in feh.items()}
# print(cel_dict)
# -----------------------------------

# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
#
# # if in output vars
# new_dict = {k: ('even No' if v % 2 == 0 else 'odd No') for (k, v) in my_dict.items()}
# print(new_dict)
# # multiple if's
# new_dict = {k: v for (k, v) in my_dict.items() if v > 3 if v % 2 == 0}
# print(new_dict)
# -----------------------------------

# nested dictionary comprehension
# AVOID as much as possible

# my_dict = {'one': {'a': 10}, 'two': {'b': 20}}
# for (external_key, external_value) in my_dict.items():
#     for (internal_key, internal_value) in external_value.items():
#         external_value.update({internal_key: float(internal_value)})
#
# # my_dict.update({external_key: external_value})
# print(my_dict)
# -----------------------------------
# -----------------------------------
# -----------------------------------

# SET COMPREHENSION

input = [1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8]

output = {var for var in input if var % 2 == 0}
print(output)
