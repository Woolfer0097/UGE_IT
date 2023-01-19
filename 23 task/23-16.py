def f(s, r):
    if r < s:
        return 0
    if r == s:
        return 1
    if r > s:
        return f(s + 1, r) + f(s * 2, r) + f(s ** 2, r)


print(f(2, 38))
