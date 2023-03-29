def tr(x):
    res = 0
    for i, num in enumerate(x):
        res += num * 21 ** (len(x) - i)
    return res


for x in range(1, 21):
    temp = []
    for y in range(1, 21):
        n1 = tr([1, 2, y, x, 9])
        n2 = tr([3, 6, y, 9, 9])
        print(n1)
        res = n1 + n2
        if res % 18 == 0:
            temp.append(True)
    if all(temp):
        print(x)
        break
