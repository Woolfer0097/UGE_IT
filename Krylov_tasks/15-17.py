def f(x, y, a):
    return (3 * x + y < a) or (x < y) or (16 <= x)


for a in range(-1000, 1000):
    if all([f(x, y, a) for x in range(1, 100) for y in range(1, 100)]):
        print(a)
        break
