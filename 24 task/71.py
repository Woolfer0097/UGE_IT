s = open("24data/k8-100.txt").read()

res = ["", 0]
t = 0
for i in range(len(s) - 1):
    a1 = s[i]
    a2 = s[i + 1]
    if a1 == a2:
        t += 1
        if t > res[1]:
            res = [a1, t + 1]
    else:
        t = 0
print(*res)
