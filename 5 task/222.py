from itertools import *


count = 0
for i in range(800, 900):
    permuts = [int("".join(i)) for i in permutations(str(i), 2) if int("".join(i)) > 10]
    if permuts:
        max_number = max(permuts)
        min_number = min(permuts)
        equation = max_number - min_number
        if equation == 30:
            count += 1

print(count)
