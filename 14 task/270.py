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


expression = 256 ** 2 + 4096 ** 16 - 15
res_base = 16
count_number = 15
# print(transfer_10_to_x(expression, res_base))
# print(sum(transfer_10_to_x(expression, res_base)))  # Сумма цифр
result_list = transfer_10_to_x(expression, res_base)
print(result_list.count(count_number))  # Подсчёт максимальных чисел
