def f(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    else:
        return f(s + 2, e) + f(s * 3, e) + f(s * 4, e)


print(f(1, 194) * f(194, 284) * f(284, 392) * f(392, 482) * f(482, 554) * f(554, 600))
