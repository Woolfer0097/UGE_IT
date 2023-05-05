data = list(map(int, open("17/17var16.txt")))

r = []
for i in range(len(data) - 1):
    p1 = data[i]
    p2 = data[i + 1]
    if (p1 > 300) or (p2 > 300):
        r.append(p1 ** 2 + p2 ** 2)

print(min(r))
