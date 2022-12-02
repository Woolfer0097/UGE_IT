def f(x1, x2, x3):
    return not(x1 * x2) and not(x2 * x3) and not(x3 * x1)


def g(x1, x2, x3):
    return not(x1 ^ x2 ^ x3 ^ 1)


print(not(f(1, 1, 1)))
print(not(g(1, 1, 1)))
