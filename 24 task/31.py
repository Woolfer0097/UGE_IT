s = open("k7b-5.txt").read()

c = "CA"
while c in s:
    c += "CA"


if c[:-1] in s:
    print(len(c) - 1)
elif c[:-2] in s:
    print(len(c) - 2)
elif c in s:
    print(len(c) - 3)
