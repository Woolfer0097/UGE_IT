from itertools import permutations

vowels = ["а"]
consonants = ["б", "р", "х", "т", "к"]
result = set()

for index, i in enumerate(permutations("бархатка")):
    correct = True
    for symbol_index in range(0, len(i) - 1):
        if (i[symbol_index] in vowels and i[symbol_index + 1] in vowels) or \
                (i[symbol_index] in consonants and i[symbol_index + 1] in consonants):
            correct = False
            break
    if correct:
        result.add(i)

print(len(result))
