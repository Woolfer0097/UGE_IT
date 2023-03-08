from itertools import permutations, combinations, product


count = 0
for i in product("POLYGON", repeat=5):
    w = "".join(i)
    print(w)
    if w[len(w) // 2] in ("O", "Y") and w == w[::-1]:
        count += 1


print(count)
