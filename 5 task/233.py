count = 0
for n in range(8, 10000):
    number = bin(n).replace("0b", "")
    if number.count("1") > number.count("0"):
        number += "0"
    else:
        number += "1"
    length = len(number)
    if length % 2 == 0:
        number = number[:length // 2 - 1] + number[length // 2 + 1:]
    else:
        number = number[:length // 2 - 1] + number[length // 2 + 2:]
    result = int(number, 2)
    print(result)
    if result == 58:
        count += 1

print(count)
