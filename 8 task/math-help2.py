count8 = 0
count = 0

for i in range(1, 216):
    count += 1
    if i % 8 == 0:
        print(i, "Делится на 8")
        count8 += 1

print(count)
print(round(count8 / count, 3))
