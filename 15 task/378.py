def f(x, a):
    return (x % a == 0 and a < 10) or (x % 44 != 0 and x % 99 != 0 and a < 10)



for A in range(1, 10000):
    if all([f(X, A) for X in range(1, 10000)]):
        print(A)
        break
