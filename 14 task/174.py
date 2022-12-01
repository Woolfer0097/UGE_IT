def transfer_10_to_x(number, base):
    result = []
    while number >= base:
        rest = number % base
        result.append(rest)
        number //= base
    rest = number % base
    result.append(rest)
    return result[::-1]


expression = 9 ** 5 + 3 ** 25 - 20
res_base = 3
# print(transfer_10_to_x(expression, res_base))
print(sum(transfer_10_to_x(expression, res_base)))  # Сумма цифр
