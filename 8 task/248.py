from itertools import product


count = 0
for i in product("const", repeat=16):
    if i[0] == "s" or i[-1] == "s":
        continue
    for index in range(0, len(i) - 1):
        if i[index] == "s":
            if i[index - 1] == i[index + 1]:
                break
        else:
            if i[index] == i[index + 1] or i[index - 1] == i[index]:
                break
    count += 1


print(count)
