string = "2" * 2 + "1" * 2023
string.replace("22", "11")
print(string)
while string.find("2111") != -1 or string.find("1112") != -1:
    string = string.replace("111", "1", 1)
    if string.find('21') != -1:
        string = string.replace("21", '12', 1)
    else:
        string = string.replace("12", '1', 1)

print(string)
