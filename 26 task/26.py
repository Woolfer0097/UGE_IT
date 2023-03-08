with open("26data/26-J1.txt", "r") as f:
    data = list(map(int, f.readlines()))[1:]


res = 0
for n in range(len(data)):
    for k in range(n + 1, len(data)):
        if data[n] + data[k] == 100:
            res += 1
            del data[k]
            break

print(res)

# 3845 - CORRECT
