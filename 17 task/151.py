result = []

with open("17data/17-1.txt", "r", encoding="utf-8") as f:
    data = [int(i) for i in f.readlines()]
    for i in range(len(data) - 1):
        p1 = data[i]
        p2 = data[i + 1]
        if (str(p1)[-1] == "6" and p1 % 3 == 0) or (str(p2)[-1] == "6" and p2 % 3 == 0):
            result.append(min(p1, p2))

print(len(result), min(result))
