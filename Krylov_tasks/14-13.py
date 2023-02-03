a = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E"}
for x in range(0, 15):
    if x >= 10:
        number = int(f"135{a[x]}7", 15) + int(f"7{a[x]}531", 15)
    else:
        number = int(f"135{x}7", 15) + int(f"7{x}531", 15)
    if number % 14 == 0:
        print(x)
        break
