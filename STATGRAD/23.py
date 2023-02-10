count = 0

with open("data/24.txt", "r") as f:
    s = f.read()
    write_flag = False
    tmp = []
    last_symbol = ""
    for i in range(len(s) - 1):
        last_symbol = s[i]
        if write_flag:
            tmp.append(last_symbol)
        else:
            if len(tmp) > 12 and tmp.count("B") > 2:
                count += 1
                tmp = []
        if last_symbol == "A":
            if write_flag:
                write_flag = False
                continue
            else:
                write_flag = True


print(count)
