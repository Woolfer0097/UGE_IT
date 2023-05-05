s = open("k7-m3.txt").read()


s = s.replace("A", " ").replace("B", " ")
c = 1
s = s.split()
for i in s:
    if 1 <= len(i) <= 4:
        print(c, len(i), i.lower().capitalize())
        c += 1
