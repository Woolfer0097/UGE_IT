n = 100
while True:
    n -= 1
    number = bin(n).replace("0b", "")
    for _ in range(3):
        if number.count("1") > number.count("0"):
            number += "0"
        elif number.count("1") == number.count("0"):
            number += number[-1]
        else:
            number += "1"

    if int(number, 2) % 2 == 0 and int(number, 2) % 4 != 0:
        print(n)
        break
