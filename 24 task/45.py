s = open("k7-m7.txt").read()
p = s.replace("A", " ").replace("B", " ").split()
mul = 1
for k in p:
    mul *= len(k)
p2 = str(sum([len(i) for i in p])) + "".join(p) + str(mul) + s.replace("C", "")
print(len(p))
print(s[:35])
print(p2[:35])
