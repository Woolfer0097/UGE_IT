s = open("k7b-6.txt").readline().strip()
s = s.replace("DAF", "*").replace("DA", "*").replace("D", "*")
c = -1000
t = 0
for i in s:
    if i == "*":
        t += 1
    else:
        if t >= c:
            c = t
        t = 0

print(c)
