def transfer_10_to_x(number, base):
    result = []
    while number >= base:
        rest = number % base
        result.append(str(rest))
        number //= base
    rest = number % base
    result.append(str(rest))
    return "".join(result[::-1])


count = 0
for n in range(1000000, 10000000):
    r = transfer_10_to_x(n, 9)
    if r[0] != "2" and r[0] != "6" and r[-2] != r[-1]:
        count += 1

print(count)
