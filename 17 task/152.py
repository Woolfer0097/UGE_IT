result = []

with open("17data/17-1.txt", "r", encoding="utf-8") as f:
    data = [int(i) for i in f.readlines()]
    for i in range(len(data) - 1):
        p1 = data[i]
        p2 = data[i + 1]
        if ((p1 % 9 == 0 and p2 % 9 != 0 and oct(p2)[-1] == "3") or
                (p2 % 9 == 0 and p1 % 9 != 0 and oct(p1)[-1] == "3")):
            result.append(max(p1, p2))

print(len(result), max(result))
