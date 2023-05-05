def f(s1, s2, m):
    if (s1 + s2) >= 63: return m % 2 == 0
    if m == 0: return 0
    v = [f(s1 + 1, s2, m - 1),
         f(s1 * 2, s2, m - 1),
         f(s1, s2 + 1, m - 1),
         f(s1, s2 * 2, m - 1)]
    return any(v) if (m - 1) % 2 == 0 else all(v)


print(*[s for s in range(1, 58) if f(5, s, 2)])
print(*[s for s in range(1, 58) if not f(5, s, 1) and f(5, s, 3)])
print(*[s for s in range(1, 58) if f(5, s, 2) or f(5, s, 4)])
