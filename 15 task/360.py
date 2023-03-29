def f(x, y, a, b):
    return (y <= ((x - 4)**2 + 2 + abs((x - 2)**2 - 16))) == ((y <= 2*x**2 - 12*x + a) or (y <= -4*x + b))


res = []
for a in range(1, 100):
    for b in range(1, 100):
        if all([f(x, y, a, b) for x in range(1, 100) for y in range(100)]):
            print(a + b)
            res.append(a)
            res.append(b)

print(sum(res))
