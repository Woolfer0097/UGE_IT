def f(s, r):
    if r > s:
        return 0
    if r == s:
        return 1
    return f(s + 2, r) + f(s * 3, r) + f(s * 4, r)


res = 1
flag = False
for i in range(2, 600):
    if res > i:
        i = res
    if f(res, i) % 2 != 0 and not flag:
        res *= f(res, i)
        flag = True
    else:
        flag = False
        continue

print(res)

# 376 - correct
