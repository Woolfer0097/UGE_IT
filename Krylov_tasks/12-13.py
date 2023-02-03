s = "1" + "5" * 25

while "15" in s or "1" in s:
    if "15" in s:
        s = s.replace("15", "5551")
    else:
        if "1" in s:
            s = s.replace("1", "5")

print(s.count("5"))
