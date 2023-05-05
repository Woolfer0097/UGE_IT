s = open("k7b-1.txt").read()

c = 'EAB'
while c in s:
    c += 'EAB'

if c[:-1] in s: #2 тип
    print(len(c) - 1)
elif c[:-2] in s: #1 тип
    print(len(c) - 2)
else:
    print(len(c) - 3) #3 тип

print(c)
