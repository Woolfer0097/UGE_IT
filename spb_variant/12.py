for m in range(1, 50):
    s = ">" + "1" * 15 + "2" * 35 + "3" * m
    while ">1" in s or ">2" in s or ">3" in s:
        if ">1" in s:
            s = s.replace(">1", "2>", 1)
        if ">2" in s:
            s = s.replace(">2", "3>", 1)
        if ">3" in s:
            s = s.replace(">3", "11>", 1)
    r = sum(list(map(int, list(s.strip(">")))))
    if len([i for i in range(1, r - 1) if r % i == 0]) == 3:
        print(m)
        break
