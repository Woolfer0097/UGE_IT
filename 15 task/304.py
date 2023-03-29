def f(x, y, a):
    return (4*y - x > a) or (x + 6*y < 210) or (3*y - 2*x < 30)


res = []
for a in range(-100, 1000):
    if all([f(x, y, a) for x in range(1, 100) for y in range(1, 100)]):
        res.append(a)

print(max(res))
