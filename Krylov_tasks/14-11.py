ex = 4 ** 700 + 4 ** 100 - 16 ** 100 - 64

count = 0
while ex > 0:
    if ex % 4 == 3:
        count += 1
    ex //= 4

print(count)
