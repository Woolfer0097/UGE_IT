def transfer_10_to_x(number, base):
    result = []
    while number >= base:
        rest = number % base
        result.append(rest)
        number //= base
    rest = number % base
    result.append(rest)
    return result[::-1]


expression = 4*25**2022-2*5**2000+125**1011-3*5**100-660
res_base = 5
count_number = 4
print(transfer_10_to_x(expression, res_base))
# print(sum(transfer_10_to_x(expression, res_base)))  # Сумма цифр
print(transfer_10_to_x(expression, res_base).count(count_number))  # Подсчёт заданного числа
