from itertools import *


for i in range(999, 100, -1):
    print(i)
    permuts = [int("".join(i)) for i in permutations(str(i), 2) if int("".join(i)) > 10]
    if permuts:
        max_number = max(permuts)
        min_number = min(permuts)
        print(max_number, min_number)
        equation = max_number - min_number
        print("eq", equation)
        if equation == 14:
            print(max_number, min_number)
            break
