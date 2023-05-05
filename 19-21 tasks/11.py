def f(s1, s2, m):
    if (s1 + s2) >= 62: return m % 2 == 0
    if m == 0: return 0
    v = [f(s1 +2, s2, m - 1),
         f(s1 * 2, s2, m - 1),
         f(s1, s2 + 2, m - 1),
         f(s1, s2 * 2, m - 1)]
    return any(v) if (m - 1) % 2 == 0 else all(v)


print(*[s for s in range(1, 55) if f(7, s, 2)])
print(*[s for s in range(1, 55) if not f(7, s, 1) and f(7, s, 3)])
print(*[s for s in range(1, 55) if (f(7, s, 2) and f(7, s, 4)) or (not f(7, s, 2) and f(7, s, 4))])
