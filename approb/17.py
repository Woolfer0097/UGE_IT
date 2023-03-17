with open("17.txt", "r") as f:
    data = list(map(int, f.readlines()))

r = []
d = len([k for k in data if k % 3 == 0])
for i in range(len(data) - 1):
    p1 = data[i]
    p2 = data[i + 1]
    if (p1 < 0 or p2 < 0) and (p1 + p2) < d:
        r.append(p1 + p2)


print(len(r), max(r))
