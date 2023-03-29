def f(x, y, a):
    return (y + 4*x != 120) or (x > a) or (y > a)


res = []
for a in range(-100, 1000):
    if all([f(x, y, a) for x in range(1, 100) for y in range(1, 100)]):
        res.append(a)

print(max(res))
