s = open("24data/k8-0.txt").read()

res = []
t = ""
maxLen = 0
for i in range(len(s) - 1):
    a1 = s[i]
    a2 = s[i + 1]
    if s[i] == s[i + 1]:
        t += a1
    else
        res.append(t + a2)
        t = ""

print(res)
for key, value in res.items():
    if value == maxLen:
        print(key, value)
