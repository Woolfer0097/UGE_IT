def transfer_x_to_base(num, base):
    result = 0
    for i, digit in enumerate(reversed(num)):
        result += int(digit) * base ** i
    return result


count = 0
first_number = ["5", "5", "1", "1", "3"]
second_number = ["7", "x", "x", "5"]
for x in range(100):
    second_number[1] = x
    second_number[2] = x
    f_n = transfer_x_to_base(first_number, x)
    s_n = transfer_x_to_base(second_number, 80)
    if abs(s_n - f_n) <= 1000000:
        count += 1

print(count)
