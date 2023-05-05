def f(s1, s2, m):
    if (s1 * s2) >= 144: return m % 2 == 0
    if m == 0: return 0
    v = [f(s1 + 1, s2, m - 1),
         f(s1 * 2, s2, m - 1),
         f(s1, s2 + 1, m - 1),
         f(s1, s2 * 2, m - 1)]
    return any(v) if m % 2 == 0 else all(v)


print(*[s for s in range(1, 141) if f(3, s, 3) and not f(3, s, 1)])
print(*[s for s in range(1, 141) if (f(3, s, 2) and not f(3, s, 4)) or (not f(3, s, 2) and f(3, s, 4))])
