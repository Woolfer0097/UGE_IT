d = {10: "A", 11: "B", 12: "C"}
for x in range(1, 13):
    if x in d.keys():
        n1 = f"753{d[x]}2"
        n2 = f"2{d[x]}173"
    else:
        n1 = f"753{x}2"
        n2 = f"2{x}173"
    r = int(n1, 13) + int(n2, 13)
    if r % 12 == 0:
        print(r // 12)
        break
