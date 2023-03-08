def f(x):
    if x == 1:
        return 0
    if x >= 2:
        return f(x - 1) + x


def g(x):
    if x == 1:
        return 1
    if x >= 2:
        return g(x - 1) + f(x - 1)


print(f(6) * g(6))
