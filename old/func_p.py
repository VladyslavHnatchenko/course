from pip._vendor.html5lib.filters.alphabeticalattributes import Filter


def processing(element, type_filter, all_data_size):
    filters = Filter(all_data_size, type_filter).get_all()
    for filt in filters:
        element = filt.filter(element)


class DataStorage(object):
    pass


def main():
    data = DataStorage().get_all_data()
    for x in data:
        processing(x, 'all', len(data))


# def f(x, y, z, a=None, b=None):
#     print(x, y, z, a, b)
#
#
# f(11, 22, 33)

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))
#
# print(list(reversed(numbers)))

# w = reduce(lambda res, x: [x]+res, [1, 2, 3, 4], [])
# print(w)

# numbers = [2, 3, 4, 5, 6]
# w = reduce(lambda res, x: res*x, numbers, 1)
# print(w)

# numbers = [10, 4, 2, -1, 6]
# w = list(filter(lambda x: x < 5, numbers))
#
# print(w)

# list1 = [7, 2, 3, 10, 12]
# list2 = [-1, 1, -5, 4, 6]
#
# list(map(lambda x, y: x*y, list1, list2))

# w = lambda x, y: x**2 + y**2
#
# print(w(2, 3))

# def calc(x, y):
#     return x**2 + y**2
#
#
# print(calc(3, 4))

# [x * 2 if x % 2 == 0 else x + 1 for x in range(5, 10)]

# for x in range(5, 10):
#     if x % 2 == 0:
#         x *= 2
#     else:
#         x += 1
