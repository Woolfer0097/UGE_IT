s = "4" * 197


while "4444" in s or "777" in s:
    if "4444" in s:
        s = s.replace("4444", "77")
    else:
        s = s.replace("777", "4")


print(s)
