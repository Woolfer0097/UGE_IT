def t(n):
    r = 0
    for index, digit in enumerate(n):
        r += digit * (55 ** (len(n) - index - 1))
    return r


res = []
for a in range(1, 100):
    n1 = t([35, a, 34, 33])
    n2 = t([2, 33, a, 34])
    if (n1 - n2) % 29 == 0:
        res.append([a, n1 - n2])


res.sort(key=lambda x: x[0])

print(abs(res[0][1] - res[-1][1]))
