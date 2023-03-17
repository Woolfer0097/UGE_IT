with open("26.txt", "r") as f:
    d = list(map(int, f.readlines()[1:]))


d.sort()
s1 = 0
s2 = 0
# print(d)
while len(d) >= 3:
    t1 = d.pop(0)
    t2 = d.pop(0)
    t3 = d.pop(-1)
    # print(t1, t2, t3)
    # print(d)
    s1 += sum([t1, t2, t3]) - max([t1, t2, t3])
    s2 += sum([t1, t2, t3]) - min([t1, t2, t3])
    # print(s1, s2)
s1 += sum(d)
s2 += sum(d)

print(s1, s2)
