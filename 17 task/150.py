result = []
with open("17data/17-1.txt", "r", encoding="utf-8") as f:
    data = [int(i) for i in f.readlines()]
    for index in range(len(data) - 1):
        p1 = data[index]
        p2 = data[index + 1]
        if (p1 % 7 == 0 and p2 % 17 != 0) or (p2 % 7 == 0 and p1 % 17 != 0):
            result.append(p1 + p2)

print(len(result), min(result))
