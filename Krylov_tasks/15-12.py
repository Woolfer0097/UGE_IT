def d(n, m):
    return n % m == 0


for a in range(100000000000, 1, -1):
    for x in range(100000000000, 1, -1):
        if d(x, a) or not (d(x, 54) or (not d(162, x))) == 1:
            print(a)
        break
    break
