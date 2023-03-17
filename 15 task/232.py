def f(x, a):
    return (x % 5940 != 0 and x % a == 0 and x % 6300 == 0) <= (x % 5940 == 0 or x % a != 0)



for A in range(1, 10000):
    if all([f(X, A) for X in range(1, 10000)]):
        print(A)
        break
