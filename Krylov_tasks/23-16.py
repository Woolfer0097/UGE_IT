def f(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    return f(s + 5, e) + f(s + 4, e) + f(s * 3, e)


print(f(2, 6) * f(6, 30))
