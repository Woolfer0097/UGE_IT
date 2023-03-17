s = open("24.txt").readline()

s = s.replace("21", "*").replace("23", "*").replace("25", "*")\
    .replace("41", "*").replace("43", "*").replace("45", "*")\
    .replace("1", " ").replace("2", " ").replace("3", " ").replace("4", " ").replace("5", " ")

print(s)
print(max([i.count("*") for i in s.split()]))

