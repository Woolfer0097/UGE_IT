def f(s, r):
    if s > r:
        return 0
    elif s == r:
        return 1
    return f(s + 2, r) + f(s * 2, r) + f(s * 3, r)


print(f(1, 6) * f(6, 28))
