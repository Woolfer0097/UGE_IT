result = []

with open("17data/17-3.txt", "r", encoding="utf-8") as f:
    data = [int(i) for i in f.readlines()]
    for i in range(len(data) - 1):
        p1 = data[i]
        p2 = data[i + 1]
        if p1 * p2 > 0 and (p1 + p2) % 7 == 0:
            result.append(p1 * p2)

print(len(result), min(result))
