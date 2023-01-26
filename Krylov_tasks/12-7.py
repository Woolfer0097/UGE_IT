string_custom = "1" * 50

while string_custom.find("11111") != -1 or string_custom.find("15") != -1:
    if string_custom.find("11111") != -1:
        string_custom = string_custom.replace("11111", "15", 1)
    else:
        string_custom = string_custom.replace("15", "1", 1)


print(string_custom)
