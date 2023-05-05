def f(s1, s2, m):
    if (s1 + s2) <= 20: return m % 2 == 0
    if m == 0: return 0
    v = [f(s1 - 1, s2, m - 1),
         f((s1 + 1) // 2, s2, m - 1),
         f(s1, s2 - 1, m - 1),
         f(s1, (s2 + 1) // 2, m - 1)]
    return any(v) if (m - 1) % 2 == 0 else all(v)


print(*[s for s in range(11, 100) if f(10, s, 2)])
print(*[s for s in range(11, 100) if not f(10, s, 1) and f(10, s, 3)])
print(*[s for s in range(11, 100) if (f(10, s, 2) and not f(10, s, 4) or \
                                      (not f(10, s, 2) and f(10, s, 4)))])
