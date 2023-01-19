def f(s, r):
    if r < s:
        return 0
    if r == s:
        return 1
    return f(sum(list(map(int, list(str(s))))), r)