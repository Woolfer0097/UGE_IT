def f(s1, s2, m):
    if (s1 + s2) >= 69: return m % 2 == 0
    if m == 0: return 0
    v = [f(s1 + 1, s2, m - 1),
         f(s1 * 2, s2, m - 1),
         f(s1, s2 + 1, m - 1),
         f(s1, s2 * 2, m - 1)]
    return any(v) if (m - 1) % 2 == 0 else all(v)


print(*[s for s in range(1, 63) if f(6, s, 2) or f(6, s, 4)])
