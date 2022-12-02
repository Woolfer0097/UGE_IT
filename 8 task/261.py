from itertools import product


count = 0
for index, i in enumerate(sorted(product("аежйму", repeat=4))):
    if index > 1000:
        is_repeated = False
        for k in range(0, len(i) - 1):
            temp = i[k]
            if temp == i[k + 1]:
                is_repeated = True
        if not is_repeated and index % 2 == 0:
            count += 1

print(count)
