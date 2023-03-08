count37 = 0
count13 = 0
count77 = 0
count = 0

for i in range(100, 1000):
    count += 1
    if i % 37 == 0:
        print(i, "Делится на 37")
        count37 += 1
    if i % 13 == 0:
        print(i, "Делится на 13")
        count13 += 1
    if i % 77 == 0:
        print(i, "Делится на 77")
        count77 += 1

print(count)
print(count37)
print(count13)
print(count77)
print(round(count37 / count, 3))
print(round(count13 / count, 3))
print(round(count77 / count, 3))
