with open("17_2491.txt", "r") as f:
    data = list(map(int, f.readlines()))

res = []
avg = sum(data) // len(data)
for i in range(len(data) - 2):
    p1 = data[i]
    p2 = data[i + 1]
    p3 = data[i + 2]
    if p1 < avg or p2 < avg or p3 < avg and "9" in str(p1) and "9" in str(p2) and "9" in str(p3):
        res.append(p1 + p2 + p3)


print(len(res), max(res))
