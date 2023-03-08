def f(x, A):
    return ((x % A == 0) and (x % 15 != 0)) <= ((x % 18 == 0) or (x % 15 == 0))


for A in range(1, 1000):
    if all([f(x, A) for x in range(1, 1000)]):
        print(A)
        break
