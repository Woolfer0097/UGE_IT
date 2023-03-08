def x4(num):
    res = []
    while num > 0:
        rest = str(num % 4)
        num //= 4
        res.append(rest)
    return "".join(res)[::-1]


count = 0
for i in range(1, 20):
    if x4(i)[0] == "2":
        count += 1

print(count)
