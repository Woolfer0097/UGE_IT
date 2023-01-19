count_max = 0

with open("24/24var09-13.txt", "r") as file:
    data = file.readline()
    count_Z = 0
    count_others = 0
    for symbol in data:
        if symbol == "Z":
            if count_Z == 1:
                count_Z = 0
                if count_max < count_others:
                    count_max = count_others
            else:
                count_Z += 1
        else:
            count_others += 1


print(count_max)
