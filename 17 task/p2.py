with open("17data/17-344.txt", "r") as file:
    data = list(map(int, file.readlines()))


res = []
minimal = min([k for k in data if k % 103 == 0])
for i in range(len(data) - 1):
    p1 = data[i]
    p2 = data[i + 1]
    if (p1 + p2) % 2 == 0 and (p1 - p2) % minimal == 0:
        res.append(p1 + p2)


print(len(res), max(res))
