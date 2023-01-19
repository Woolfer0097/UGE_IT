from numpy import multiply


result = []


with open("17/17var11.txt", "r", encoding="utf-8") as file:
    data = list(map(int, file.readlines()))
    for i in range(len(data) - 1):
        current = data[i]
        nextt = data[i + 1]
        if int(str(current)[-1]) % 2 != 0 and \
                int(str(nextt)[-1]) % 2 != 0 and \
                str(current)[-1] == str(nextt)[-1]:
            result.append([current, nextt])


print(len(result), max([x * y for (x, y) in result]))
