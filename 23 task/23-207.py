def f(s, r):
    if r > s:
        return 0
    if r == s:
        return 1
    return f(s - 1, r) + f(s // 2, r)


print(f(30, 12) * f(12, 1))


# 376 - correct
