with open("17data/17-343.txt", "r") as f:
    data = list(map(int, f.readlines()))


res = []
for i in range(len(data) - 2):
    p1 = data[i]
    p2 = data[i + 1]
    p3 = data[i + 2]
    if sum([int(d) for i, d in enumerate(str(p1)) if i % 2 != 0]) %\
            sum([int(d) for i, d in enumerate(str(p1)) if i % 2 == 0])\
            == 0:
        res.append(p1 + p2 + p3)


print(len(res), min(res))

