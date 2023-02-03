result = []

with open("17/17var14.txt", "r", encoding="utf-8") as file_read:
    data = [int(i) for i in file_read.readlines()]
    for j in range(len(data) - 1):
        n1 = data[j]
        n2 = data[j + 1]
        if n1 + n2 >= 50 and n1 > 0 and n2 > 0:
            result.append(n1 * n2)

print(len(result), min(result))
