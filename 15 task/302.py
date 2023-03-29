def f(x, y, a):
    return (5*y + 4*x > a) or (2*x + 3*y < 92) or (y - 2*x < -150)


res = []
for a in range(-100, 100):
    if all([f(x, y, a) for x in range(1, 100) for y in range(1, 100)]):
        res.append(a)

print(max(res))
