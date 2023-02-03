from itertools import product

count = 0
variables = set(["".join(j) for j in product("настя", repeat=7)])
for i in variables:
    if i.count("н") == 2 and i.count("а") >= 1:
        count += 1

print(count)
