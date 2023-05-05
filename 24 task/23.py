s = open("k7a-3.txt").read()

s = s.replace("A", "*").replace("B", "*").replace("E", "*").replace("F", "*")
c = 1000
while "*" * c not in s:
    c -= 1
print(c)
