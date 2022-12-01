from itertools import product

count = 0
vars = set(["".join(i) for i in product("джобс", repeat=6)])

for i in vars:
    if i.count("д") == 1 and i.count("о") == 1 and i.count("с") == 1 and i.count("ж") <= 2:
        count += 1

print(count)
