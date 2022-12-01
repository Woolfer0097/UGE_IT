def transfer_x_10(number, base):
    res = 0
    for i, digit in enumerate(reversed(number)):
        res += digit * base ** i
    return res


divided_by_29 = []
for a in range(55):
    first_number = transfer_x_10([25, a, 24, 23], 55)
    second_number = transfer_x_10([2, 23, a, 24], 55)
    result = (first_number - second_number)
    if result % 29 == 0:
        divided_by_29.append(result)

print(abs(max(divided_by_29) - min(divided_by_29)))

