def f(s, r):
    if s > r:
        return 0
    if s == r:
        return 1
    if s < r:
        return f(s + 1, r) + f(s + 2, r)


print(f(5, 10) * f(10, 15))
