res = []
with open("26data/26-94.txt", "r") as f:
    n, k = map(int, f.readline().split())
    for i in range(n):
        floor, row, occupied = map(int, f.readline().split())
        if occupied < k:
            if k - occupied >= 4:
                res.append([row, floor])
        else:
            if k - 1 >= 4:
                res.append([row, floor])


res.sort(key=lambda x: x[0])
print(*res[-1])