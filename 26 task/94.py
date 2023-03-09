res = []
with open("26data/26-94.txt", "r") as f:
    n, k = map(int, f.readline().split())
    for i in range(n):
        floor, row, occupied = map(int, f.readline().split())
        if occupied <= k // 2:
            if k - occupied > 4:
                res.append(row)
        elif k > occupied > k // 2:
            if k - (k - occupied) > 4:
                res.append(row)
        elif occupied == k:
            if k - 1 >= 4:
                res.append(row)

print(max(res), len(res))
