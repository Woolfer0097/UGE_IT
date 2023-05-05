from math import sqrt

for a in range(244143, 367821 + 1):
    divs = set()
    if int(sqrt(a)) ** 2 == a:
        for i in range(1, int(sqrt(a)) + 1):
            if a % i == 0:
                divs.add(i)
                divs.add(a // i)
    else:
        for i in range(1, int(sqrt(a)) + 1):
            if a % i == 0:
                divs.add(i)
                divs.add(a // i)
    if len(set(divs)) == 5:
        print(*sorted(divs))
