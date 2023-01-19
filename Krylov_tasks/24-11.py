maximum = 0
count = 0


with open("24/24var09-13.txt", "r", encoding="utf-8") as file:
    for symbol in file.readline():
        if symbol != "Z":
            count += 1
        else:
            if maximum < count:
                maximum = count
                count = 0


print(maximum)
