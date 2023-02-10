result = []

with open("17data/17-1.txt", "r", encoding="utf-8") as f:
    data = [int(i) for i in f.readlines()]
    for i in range(len(data) - 1):
        p1 = data[i]
        p2 = data[i + 1]
        if p2 > p1:
            result.append(abs(p1 - p2))

print(len(result), min(result))
