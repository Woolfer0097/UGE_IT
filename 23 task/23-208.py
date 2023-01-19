def f(s, r):
    if r > s:
        return 0
    if r == s:
        return 1
    return f(s - 2, r) + f(s // 2, r)


print(f(28, 10) * f(10, 1))


# 36 - correct
