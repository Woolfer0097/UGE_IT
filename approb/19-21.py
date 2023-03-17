def f(s, c, m):
    if s >= 351:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(s + 1, c + 1, m), f(s + 4, c + 1, m), f(s * 2, c + 1, m)]

    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for S in range(1, 351):
    for M in range(1, 5):
        if f(S, 0, M) == 1:
            if M == 3:
                print(S, M)
                break
