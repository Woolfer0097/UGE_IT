from itertools import product, permutations

result = []
for i in permutations("мари", 4):
    for k in product("ина", repeat=4):
        result.append("".join(i) + "".join(k))
result.sort()
print(result.index("марианна") + 1)
