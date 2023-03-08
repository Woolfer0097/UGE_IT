def f(n, m):
    return n % m != 0


for A in range(1, 1000):
    for B in range(10, 41):
        if all([A or (not B or x % 6 == 0) for x in range(1, 1000)]):
            print(A)
            break
