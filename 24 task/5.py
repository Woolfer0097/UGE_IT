s = open("k7-25.txt").read()

c = 1000
while "C" * c not in s:
    c -= 1
print(c)
