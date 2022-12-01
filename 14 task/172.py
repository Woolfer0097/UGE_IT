def transfer_10_to_x(number, base):
    result = []
    while number >= base:
        rest = number % base
        result.append(rest)
        number //= base
    rest = number % base
    result.append(rest)
    return result[::-1]


expression = 9 ** 9 + 3 ** 21 - 7
res_base = 3
# print(transfer_10_to_x(expression, res_base))
print(transfer_10_to_x(expression, res_base).count(0))  # Подсчёт нулей
