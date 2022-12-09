from itertools import permutations


count = 0
for i in permutations("кусать", 5):
    print(i)
    if i[0] == "ь":
        break
    if "сук" not in "".join(i):
        count += 1


print(count)
