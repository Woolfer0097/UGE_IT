def f(s, r):
    if s < r:
        return 0
    if s == r:
        return 1
    return f(s - 1, r) + f(s // 3, r)


print(f(37, 10) * f(10, 2))
