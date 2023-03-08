for x in range(30):
    for y in range(30):
        for z in range(30):
            s = "0" + "1" * x + "2" * y + "3" * z

            while "01" in s or "02" in s or "03" in s:
                if "01" in s:
                    s = s.replace("01", "302", 1)
                if "02" in s:
                    s = s.replace("02", "3103", 1)
                if "03" in s:
                    s = s.replace("03", "20", 1)
            if s.count("1") == 28 and s.count("2") == 34 and s.count("3") == 45:
                print(x)


# 17 - CORRECT
