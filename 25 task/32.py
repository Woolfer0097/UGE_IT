from math import sqrt


res = []
for a in range(394441, 394505 + 1):
    dels = set()
    if int(sqrt(a)) ** 2 != a:
        for x in range(1, int(sqrt(a))):
            dels.add(x)
            dels.add(a // x)
    else:
        for x in range(1, int(sqrt(a)) + 1):
            dels.add(x)
            dels.add(a // x)
    res.append([a, len(dels), sorted(dels, reverse=True)[:2]])


res = sorted(res, key=lambda x: x[1])
print(*res)
print(res[0][1], *res[0][2])
