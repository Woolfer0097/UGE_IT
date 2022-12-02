from itertools import permutations

vowels = ["о", "а"]
consonants = ["в", "т", "р"]
count = 0

for index, i in enumerate(permutations("авторота")):
    temp = ""
    correct = True
    for symbol_index in range(len(i)):
        if (temp in vowels and i[symbol_index + 1] in vowels) or \
                (temp in consonants and i[symbol_index + 1] in consonants):
            correct = False
        else:
            temp += i[symbol_index]
    if correct:
        count += 1

print(count)
