def transfer_10_to_x(number, base):
    result = []
    while number >= base:
        rest = number % base
        result.append(str(rest))
        number //= base
    rest = number % base
    result.append(str(rest))
    return "".join(result[::-1])


def check_digits(number):
    maximum_number = 0
    for i in str(number):
        if int(i) != 0:
            if int(i) >= maximum_number:
                maximum_number = int(i)
            else:
                return False
    return True

num = 432
print(2, transfer_10_to_x(num, 2), check_digits(transfer_10_to_x(num, 2)))
print(3, transfer_10_to_x(num, 3), check_digits(transfer_10_to_x(num, 3)))
print(4, transfer_10_to_x(num, 4), check_digits(transfer_10_to_x(num, 4)))
print(5, transfer_10_to_x(num, 5), check_digits(transfer_10_to_x(num, 5)))
print(6, transfer_10_to_x(num, 6), check_digits(transfer_10_to_x(num, 6)))
print(7, transfer_10_to_x(num, 7), check_digits(transfer_10_to_x(num, 7)))
print(8, transfer_10_to_x(num, 8), check_digits(transfer_10_to_x(num, 8)))
print(9, transfer_10_to_x(num, 9), check_digits(transfer_10_to_x(num, 9)))
print(10, transfer_10_to_x(num, 10), check_digits(transfer_10_to_x(num, 10)))
