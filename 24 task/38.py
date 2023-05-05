s = open("k7c-6.txt").read()


c = 0
for i in range(len(s) - 2):
    m1 = s[i]
    m2 = s[i + 1]
    m3 = s[i + 2]
    if m1 != m3 and m1 != m2 and m2 != m3:
        c += 1
print(c)
