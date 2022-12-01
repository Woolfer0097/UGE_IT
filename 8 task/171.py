from itertools import product

count = 0
vars = set(["".join(j) for j in product("воробей", repeat=5)])
for i in vars:
    if i[0] != "й" and i[-1] != "й" and \
        "йе" not in i and "ей" not in i and \
        "ейе" not in i and i.count("й") <= 1:
        count += 1

print(count)
