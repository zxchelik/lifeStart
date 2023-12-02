a = 3
for i in range(1, 2021):
    print(i, a)
    a = (a * a * a) % 46
