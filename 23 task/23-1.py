def f(start, res):
    if res < start:
        return 0
    if res == start:
        return 1
    K = f(start, res - 1)
    if res % 2 == 0:
        K += f(start, res // 2)
    return K


print(f(1, 16))

# 36 - correct
