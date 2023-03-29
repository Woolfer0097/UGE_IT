def f(x, y, a):
    return (21*y - 5*x != -99) or (2*x - 7 > a) or (y**2 + 16 > a)


res = []
for a in range(-100, 1000):
    if all([f(x, y, a) for x in range(1, 100) for y in range(1, 100)]):
        res.append(a)

print(max(res))
