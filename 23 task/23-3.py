def f(s, r):
    if r < s:
        return 0
    if r == s:
        return 1
    K = f(s, r - 1)
    if r % 2 == 0:
        K += f(s, r // 2)
    if r % 3 == 0:
        K += f(s, r // 3)
    return K


print(f(1, 18))

# 96 - correct
