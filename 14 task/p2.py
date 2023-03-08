def t(n, b):
    res = 0
    for i in range(len(n)):
        res += n[i] * b ** (len(n) - 1 - i)
    return res


for x in range(130):
    n1 = [2, 3, x, 3, 2]
    n2 = [3, x, 2, 5, 3]
    result = t(n1, 130) + t(n2, 130)
    if result % 23 == 0:
        print(result // 23)
        break
