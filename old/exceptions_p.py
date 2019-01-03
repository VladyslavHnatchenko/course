def simple_func(value):
    assert type(value) == int
    assert value > 0

    return value * value


print(simple_func(2))
# print(simple_func(2.0))
# print(simple_func("eee"))
# print(simple_func(set()))

# try:
#     file_path = "test_file.txt"
#     with open(file_path, 'r') as fio:
#         result = fio.readlines()
#     if not result:
#         raise Exception("File is empty")
#
# except IOError as e:
#     result = []
# except Exception as e:
#     result = []
#     print(e)

# try:
#     a = 100
#     b = 0
#     c = a / b
# except ZeroDivisionError as e:
#     c = -1

# try:
#     a = 100
#     b = 0
#     c = a / b
# except ZeroDivisionError as e:
#     print(e)

# p = 100 / 0
# print(p)
