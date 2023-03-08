def f(x, A):
    return x % A == 0


B = range(50, 71)

for A in range(1, 10000):
    for x in range(1, 1000):
        if f(x, A) or (not f(x, A)) or x not in B:
            print(A)