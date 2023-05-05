s = open("k7c-1.txt").read()


c = 0
for i in range(len(s) - 2):
    m1 = s[i]
    m2 = s[i + 1]
    m3 = s[i + 2]
    if m1 in ["B", "C", "D"] and m2 in ["B", "E", "D"] and\
       m3 in ["B", "C", "E"] and m2 != m1 and m3 != m2:
        c += 1
print(c)
