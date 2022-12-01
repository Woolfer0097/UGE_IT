def transfer_10_to_x(number, base):
    result = []
    while number >= base:
        rest = number % base
        result.append(rest)
        number //= base
    rest = number % base
    result.append(rest)
    return result[::-1]


def transfer_x_to_10(number, base):
    result = 0
    for i, digit in enumerate(reversed(list(str(number)))):
        result += int(digit) * base ** i
    return result


expression = 3 * 16 ** (transfer_x_to_10(46, 8)) + 5 * 4 ** (transfer_x_to_10(40, 16)) - 8 ** \
             (transfer_x_to_10(47, 8) - int("0x1b", 0)) - 2 ** (transfer_x_to_10(110101, 2) +
                                                             transfer_x_to_10(13, 8)) + 15
res_base = 16
count_number = 3
# print(transfer_10_to_x(expression, res_base))
# print(sum(transfer_10_to_x(expression, res_base)))  # Сумма цифр
result_list = transfer_10_to_x(expression, res_base)
print(result_list.count(max(result_list)))  # Подсчёт максимальных чисел
