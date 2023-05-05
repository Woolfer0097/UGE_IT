def f(s1, s2, m):
    if (s1 + s2) >= 57: return m % 2 == 0
    if m == 0: return 0
    v = [f(s1, s2 + 1, m - 1),
         f(s1, s2 * 2, m - 1),
         f(s1 + 1, s2, m - 1),
         f(s1 * 2, s2, m - 1)]
    return any(v) if (m - 1) % 2 == 0 else all(v)


print(19)
print(*[s for s in range(1, 52) if (f(5, s, 2))])
print(*[s for s in range(1, 52) if (f(5, s, 3) and not f(5, s, 1))])
print(*[s for s in range(1, 52) if (f(5, s, 2) or f(5, s, 4))])
