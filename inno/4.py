res = [[0, 0] for i in range(100)]

for i in range(10):
    d1, d2 = map(int, input().split())
    res[d1*13 + d2] = [d1, d2]
    print(res)
