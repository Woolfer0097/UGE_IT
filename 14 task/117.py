def transfer_10_to_x(number, base):
    result = []
    while number >= base:
        rest = number % base
        result.append(rest)
        number //= base
    rest = number % base
    result.append(rest)
    return result[::-1]


expression = 4 ** 2015 + 8 ** 2016 - 2 ** 2017 - 150
res_base = 2
count_number = 0
print(transfer_10_to_x(expression, res_base))
# print(sum(transfer_10_to_x(expression, res_base)))  # Сумма цифр
print(transfer_10_to_x(expression, res_base).count(count_number))  # Подсчёт заданного числа
