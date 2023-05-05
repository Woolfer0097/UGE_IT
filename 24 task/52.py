s = open("k8-0.txt").read()

m = -1
t = 0
for i in range(len(s) - 1):
    p1 = s[i]
    p2 = s[i + 1]
    if p1 == p2:
        t += 1
    else:
        if t >= m:
            res = [p1, t + 1]
        t = 0
print(*res)
