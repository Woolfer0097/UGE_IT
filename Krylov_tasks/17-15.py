data = list(map(int, open("17/17var15.txt").readlines()))

r = []
for i in range(len(data) - 1):
    p1 = data[i]
    p2 = data[i + 1]
    if p1 > 700 or p2 > 700:
        r.append(p1**2 + p2**2)


print(len(r), max(r))
