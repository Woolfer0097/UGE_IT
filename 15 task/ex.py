def F(x, A):
    return (x % A != 0) <= ((x % 16 == 0) <= (x % 24 != 0))


for A in range(1, 10 ** 20):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
