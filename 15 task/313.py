def f(x, y, a):
    return (5*y + 7*x != 129) or (3*x > a) or (4*y > a)


res = []
for a in range(-100, 1000):
    if all([f(x, y, a) for x in range(1, 100) for y in range(1, 100)]):
        res.append(a)

print(max(res))
