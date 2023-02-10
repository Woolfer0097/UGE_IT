def m(k):
    return 7000000 + k


c = 0
while c < 6:
    for i in range(2, 1000000):
        res = m(i)
        dels = [j for j in range(2, res) if res % j == 0]
        for g in range(len(dels) - 2):
            f = dels[g]
            s = dels[g + 1]
            th = dels[g + 2]
            if f * s * th == res and f != s and f != th and s != th:
                print(i)
                c += 1
