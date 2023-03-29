def f(x, y, a):
    return (7*x + 2*y > 17) or (x < a and y <= a)


res = []
for a in range(-100, 1000):
    if all([f(x, y, a) for x in range(1, 100) for y in range(1, 100)]):
        print(a)
        break

