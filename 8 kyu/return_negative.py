# In this simple assignment you are given a number and have to make it negative.
# But maybe the number is already negative?

# def make_negative(number):
#     if number >= 0:
#         return 0 - number
#     else:
#         return number
#
#
# print(make_negative(10))
# print(make_negative(0))
# print(make_negative(-50))


def make_negative(number):
    return -abs(number)


print(make_negative(10))
print(make_negative(0))
print(make_negative(-50))
