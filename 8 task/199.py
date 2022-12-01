from itertools import product


count = 0
for i in product("aedcb", repeat=4):
    if sorted(i[:2]) == list(i[:2]) and sorted(i[2:], reverse=True) == list(i[2:]):
        for index, j in enumerate(i):
            if j in "bcd":
                if "a" not in i[index:] and "e" not in i[index:]:
                    count += 1
                    break

print(count)
