def f(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s + 3, e) + f(s + 4, e) + f(s * 3, e)


print(f(1, 7) * f(7, 30))
