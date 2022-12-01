def transfer_10_to_x(number, base):
    res = []
    while number > 0:
        rest = number % base
        res.append(str(rest))
        number //= base
    return int("".join(res[::-1]))


def transfer_x_to_10(number):
    result = 0
    for i, digit in enumerate(reversed(list(str(number)))):
        result += int(digit) * 100 ** i
    return result


count = 0
for x in range(2, 100):
    first_number = transfer_10_to_x(13152, x)
    second_number = transfer_10_to_x(int(f"7{x}25"), 100)
    result = transfer_x_to_10(first_number) + transfer_x_to_10(second_number)
    if result % 11 == 0:
        print(result)
        count += 1

print(count)
