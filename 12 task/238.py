s = ">" + "1" * 15 + "2" * 20 + "3" * 25


while ">1" in s or ">2" in s or ">3" in s:
    if ">1" in s:
        s = s.replace(">1", "22>", 1)
    if ">2" in s:
        s = s.replace(">2", "2>1")
    if ">3" in s:
        s = s.replace(">3", "1>")


print(sum(list(map(int, s.strip(">")))))


# 205 - CORRECT
