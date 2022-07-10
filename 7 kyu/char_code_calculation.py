def calc(x):
    asc_values = []

    for k in x:
        asc_values.append(ord(k))

    total1 = "".join(map(str, asc_values))
    total2 = total1.replace("7", "1")

    x = 0
    y = 0

    for i in total1:
        x += int(i)

    for j in total2:
        y += int(j)

    return x - y


print(calc("abc"))
