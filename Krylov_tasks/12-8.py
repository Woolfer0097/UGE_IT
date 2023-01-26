s = "1" * 65

while s.find("11111") != -1 or s.find("15") != -1:
    if s.find("11111") != -1:
        s = s.replace("11111", "15", 1)
    else:
        s = s.replace("15", "1", 1)


print(s)
