data = []
with open("data/26.txt", "r") as f:
    raw = f.readlines()
    n = int(raw[0])
    for j in range(n - 2):
        data.append(list(map(int, raw[j + 1].split())))

rows = [k[0] for k in data]
cols = [k[1] for k in data]
print(sorted(cols))

max_row = [0, 0]

for row in range(9998, 0, -1):
    count = 0
    for col in range(9998, 0, -2):
        for i in data[row]:
            if

                count += 1
    if max_row[0] < count:
        max_row = [count, row]


print(" ".join(map(str, max_row)))
