def f(s, r):
    if r > s:
        return 0
    if r == s:
        return 1
    return f(s - 1, r) + f(s // 3, r)


print(f(33, 9) * f(9, 1))
