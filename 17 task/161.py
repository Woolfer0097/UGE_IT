result = []

with open("17data/17-3.txt", "r", encoding="utf-8") as f:
    data = [int(i) for i in f.readlines()]
    for i in range(len(data) - 1):
        p1 = data[i]
        p2 = data[i + 1]
        if (p1 + p2) % 2 == 0 and str(p1 + p2)[-1] != "6":
            result.append((p1 + p2) // 2)

print(len(result), max(result))
