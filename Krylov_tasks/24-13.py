with open("24/24var09-13.txt", "r", encoding="utf-8") as f:
    max_count = 0
    count_z = 0
    count_others = 0
    for i in f.readline().lower():
        if i == "z":
            count_z += 1
        if count_z == 3:
            if count_others > max_count:
                max_count = count_others
                count_z = 0
                count_others = 0
        else:
            count_others += 1

print(max_count)
