def f(x, a):
    return (x % a == 0) or (x % 180 != 0) or ((x % 130 == 0) and (a < 100))



for A in range(1, 1000):
    if all([f(X, A) for X in range(1, 1000)]):
        print(A)
        break
