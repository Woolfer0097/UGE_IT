def transfer_10_to_x(number, base):
    result = []
    while number >= base:
        rest = number % base
        result.append(rest)
        number //= base
    rest = number % base
    result.append(rest)
    return result[::-1]


expression = 32 ** 30 + 8 ** 60 - 32
res_base = 4
count_number = 3
# print(transfer_10_to_x(expression, res_base))
# print(sum(transfer_10_to_x(expression, res_base)))  # Сумма цифр
print(transfer_10_to_x(expression, res_base).count(count_number))  # Подсчёт заданного числа
print(transfer_10_to_x(211, 5))
