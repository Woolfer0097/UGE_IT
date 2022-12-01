from itertools import permutations


count = 0
for i in list(permutations("ТИКТОК")):
    for j in range(1, len(i) - 1):
        if i[j] == i[j - 1] or i[j] == i[j + 1]:
            break
        else:
            count += 1
            break

print(count)
