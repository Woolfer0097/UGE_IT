data = list(map(int, open("17/17var17.txt").readlines()))

r = []
for i in range(len(data) - 1):
    p1 = data[i]
    p2 = data[i+1]
    if p1 < 450 and p2 < 450:
        r.append(p1 ** 3 + p2 ** 3)


print(len(r), max(r))
