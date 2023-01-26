string_custom = "1" * 2022
while string_custom.find("11") != -1 or string_custom.find("555") != -1:
    if string_custom.find("11") != -1:
        string_custom = string_custom.replace("11", "555")
    else:
        string_custom = string_custom.replace("555", "5")


print(string_custom)
