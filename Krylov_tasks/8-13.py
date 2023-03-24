import itertools

a = [0, 1, 2, 3, 4, 5, 6, 7]

c = 0
for number in itertools.product(a, repeat=4):
    nc1 = number.count(number[0])
    nc2 = number.count(number[1])
    nc3 = number.count(number[2])
    nc4 = number.count(number[3])
    if (number[0] == number[1] and nc1 == 2 and nc3 < 2 and nc4 < 2) or\
            (number[1] == number[2] and nc2 == 2 and nc1 < 2 and nc4 < 2) or\
            (number[2] == number[3] and nc3 == 2 and nc1 < 2 and nc2 < 2):
        print(number)
        c += 1

print(c)