res = []
f = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G"}
for x in range(2, 17):
    if x > 9:
        e = int(f"10{f[x]}0", 17) + int(f"F0{f[x]}FF", 17)
    else:
        e = int(f"10{x}0", 17) + int(f"F0{x}FF", 17)
    if e % 13 == 0:
        res.append([x, e // 13])
res.sort(key=lambda l: l[0], reverse=True)
print(res)
print(res[0][0], res[0][1])
