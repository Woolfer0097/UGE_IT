def f(x, y, a):
    return (2 * y - x < a) or (x + 2 * y > 50) or (2 * x + y < 40)


for a in range(1, 1000):
    if all([f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)]):
        print(a)
        break
