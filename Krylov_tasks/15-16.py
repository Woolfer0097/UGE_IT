def f(x, y, a):
    return not((x < a) and (y < a) and (x*y > 1200))


for A in range(0, 1000):
    if all([f(X, Y, A) for X in range(1, 100) for Y in range(1, 100)]):
        print(A)
