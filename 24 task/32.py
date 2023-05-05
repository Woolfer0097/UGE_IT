s = open("k7b-6.txt").read()

c = "DAF"
while c in s:
    c += "DAF"


if c[:-1] in s:
    print(len(c) - 1)
elif c[:-2] in s:
    print(len(c) - 2)
elif c in s:
    print(len(c) - 3)
