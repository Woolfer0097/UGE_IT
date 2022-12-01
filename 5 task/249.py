for n in range(90, 100):
    number = str(bin(n))[2:]
    if number.count("1") == number.count("0"):
        number += number[-1]
    else:
        if number.count("1") > number.count("0"):
            number += "0"
        else:
            number += "1"
    if number.count("1") == number.count("0"):
        number += number[-1]
    else:
        if number.count("1") > number.count("0"):
            number += "0"
        else:
            number += "1"
    if number.count("1") == number.count("0"):
        number += number[-1]
    else:
        if number.count("1") > number.count("0"):
            number += "0"
        else:
            number += "1"
    result_number = int(number, 2)
    if result_number > 90 and result_number % 2 == 0 and result_number % 4 != 0:
        print(n)

