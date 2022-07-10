import math


def is_square(n):
    if n < 0:
        return False

    x = math.sqrt(n)

    return x.is_integer()


print(is_square(25))
print(is_square(0))
print(is_square(-1))
print(is_square(2))
print(is_square(16))
