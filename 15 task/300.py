def f(x, y, a):
    return (y - x > a) or (x + 4 * y > 40) or (y - 2 * x < -35)


res = []
for a in range(-100, 100):
    if all([f(x, y, a) for x in range(1, 100) for y in range(1, 100)]):
        res.append(a)

print(max(res))
