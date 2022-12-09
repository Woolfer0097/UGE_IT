from itertools import permutations

result = set()
for index, i in enumerate(permutations("спортлото")):
    if i[0] != "о" and i[-1] != "о":
        result.add(i)

print(len(result) - 1)
