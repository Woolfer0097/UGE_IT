def f(x, a):
    return (x % a != 0 or x % 36 == 0 and x % 126 == 0) and (a > 1000)


for a in range(1, 100000):
    if all([f(x, a) for x in range(1, 1000)]):
        print(a)
        break
