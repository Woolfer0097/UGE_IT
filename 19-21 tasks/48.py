def f(s, m):
    if 43 <= s <= 72: return m % 2 == 0
    if s >= 72: return (m - 1) % 2 == 0
    if m == 0: return 0
    v = [f(s+1, m - 1),
         f(s*2, m - 1),
         f(s*3, m - 1)]
    return any(v) if (m - 1) % 2 == 0 else all(v)


print(*[s for s in range(1, 43) if f(s, 2)])
print(*[s for s in range(1, 43) if not f(s, 1) and f(s, 3)])
print(*[s for s in range(1, 43) if (not f(s, 2) and f(s, 4)) or (f(s, 2) and not f(s, 4))])
