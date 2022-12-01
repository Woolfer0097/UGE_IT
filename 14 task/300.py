def transfer_10_to_x(number, base):
    result = []
    while number >= base:
        rest = number % base
        result.append(rest)
        number //= base
    rest = number % base
    result.append(rest)
    return result[::-1]


expression = 7 ** 103 + 20 * 7 ** 204 - 3 * 7 ** 57 + 97
res_base = 7
count_number = 6
# print(transfer_10_to_x(expression, res_base))
# print(sum(transfer_10_to_x(expression, res_base)))  # Сумма цифр
print(transfer_10_to_x(expression, res_base).count(count_number))  # Подсчёт заданного числа
