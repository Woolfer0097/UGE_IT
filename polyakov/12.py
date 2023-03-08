def editor(line):
    while "21" in line or "31" in line or "32" in line:
        if "21" in line:
            line = line.replace("21", "12 task")
        if "31" in line:
            line = line.replace("31", "13")
        if "32" in line:
            line = line.replace("32", "23")
    return line


for n in range(1, 100):
    s = "1" * n + "2" * n + "3" * n
    res = editor(s)
    if len(res) > 51:
        if editor(s)[51] == "2":
            print(n)
            break
