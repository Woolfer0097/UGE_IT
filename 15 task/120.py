def f(x, A):
    return ((x % A != 0) and (x % 6 == 0)) <= (x % 3 != 0)


for A in range(1, 1000):
    if all([f(x, A) for x in range(1, 1000)]):
        print(A)
