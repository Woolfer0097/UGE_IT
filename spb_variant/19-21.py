def f(s, c, m):
    if s < 12:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(s // 3, c + 1, m), f(s - 12, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


c = 0
for s in range(13, 500):
    for m in range(1, 5):
        if f(s, 0, m):
            if m == 4:
                c += 1
                break

print(c)
