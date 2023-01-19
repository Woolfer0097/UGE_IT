def f(s, r):
    if r < s:
        return 0
    if r == s:
        return 1
    if r > s:
        return f(s + 1, r) + f(s + 2, r) + f(s * 2, r)


print(f(3, 13) - (f(3, 8) * f(8, 13)))
