def f(x, y, a):
    return (3*y + 2*x != 72) or (a > x and a > y)


res = []
for a in range(10, 100):
    if all([f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)]):
        print(a)
        break

