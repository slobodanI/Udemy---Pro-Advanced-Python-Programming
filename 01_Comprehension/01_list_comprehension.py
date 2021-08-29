# # intersection of lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 3, 4, 5, 6]
#
# intersection = [x for x in list1 for y in list2 if x == y]
# print(intersection)
#
# non_common_el = [(x, y) for x in list1 for y in list2 if x != y]
# print(non_common_el)
# ------------------------------------

# my_list = ['Hello World', "Python", 'Java', 'C']
#
# x = [i.lower() for i in my_list]
# print(x)
# ------------------------------------

# list1 = [1, 2, 3, 4, 5]
# x = [[a**2, a**3] for a in list1]
#
# print(x)
# ------------------------------------

# res = list(map(lambda x: x, 'Hello'))
# print(res)
# ------------------------------------

# with open("file_to_read.txt", "r") as op:
#     output = [i for i in op if "bla" in i]
#     print(output)
# ------------------------------------

def x(a):
    return a * 2


y = [x(a) for a in range(10) if a % 2 == 0]
print(y)
# ------------------------------------
