s = open("24.txt").readline()
s = s.replace("CFE", "*").replace("FCE", "*").replace("C", " ")\
    .replace("D", " ").replace("E", " ").replace("F", " ")

for c in s.split():
    print(c)
