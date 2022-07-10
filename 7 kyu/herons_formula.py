import math


def heron(a, b, c):
    s = (a + b + c) / 2
    triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return round(triangle_area, 2)


print(heron(11, 16, 25))
