def f(x, a):
    return (x % 36 != 0 or x % 42 != 0 or x % a == 0) and (a * (a - 25) < 25 * (a + 200))


for a in range(1, 100000):
    if all([f(x, a) for x in range(1, 1000)]):
        print(a)
        break
