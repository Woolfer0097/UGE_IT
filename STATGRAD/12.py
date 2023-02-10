def f(s):
    while "00" not in s:
        s = s.replace("021", "102")
        s = s.replace("022", "301")
        s = s.replace("02", "20")
        s = s.replace("01", "10")
    return s


start = "0"


for x in range(10000):
    for y in range(1, 3):
        start += str(y)
        start += "0"
        res = f(start)
        if res.count("1") == 27 and res.count("2") == 9 and res.count("3") == 4:
            print(start)
            break
        else:
            if start[-2] == "1":
                start = start[:-2]
            else:
                start = start[:-1]
