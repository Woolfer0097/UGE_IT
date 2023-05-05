s = open("24/24var14-20.txt").read()


for a in range(9, 0, -1):
    for b in range(a - 1, 0, -1):
        for c in range(b - 1, 0, -1):
            for d in range(c - 1, 0, -1):
                for e in range(d - 1, 0, -1):
                    for f in range(e - 1, 0, -1):
                        for g in range(f - 1, 0, -1):
                            r = f"{a}{b}{c}{d}{e}{f}{g}"
                            if r in s:
                                print(len(r), r)
                                break
