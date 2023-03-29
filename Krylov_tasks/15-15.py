def f(x, y, a):
    return (x < a) and (y < a) and (x*y > 601)


for a in range(1, 1000):
    if all([f(x, y, a) == 0 for x in range(1, 100) for y in range(1, 100)]):
        print(a)

