def f(x, a):
    return (x % a != 0) or (x % 21 == 0) or (x % 15 != 0)


for A in range(1, 1000):
    if all([f(x, A) for x in range(1, 1000)]):
        print(A)
        break

