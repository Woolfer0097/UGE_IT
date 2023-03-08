with open("17-345.txt", "r") as fd:
    data = [int(i) for i in fd.readlines()]


res = []
x = [k for k in data if str(k)[-2:] == "52"]
r = max(x) - min(x)
for i in range(len(data) - 1):
    e1 = data[i]
    e2 = data[i + 1]
    if (e1 < r < e2) or (e1 > r > e2):
        res.append(e1 + e2)


print(len(res), max(res))
