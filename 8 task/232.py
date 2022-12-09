def transfer_10_to_x(number, base):
    result = []
    while number > 0:
        rest = number % base
        result.append(str(rest))
        number //= base
    return "".join(result[::-1])


count = 0
for n in range(100000, 1000000000):
    r = transfer_10_to_x(n, 9)
    if len(r) > 7:
        break
    if r[0] != "2" and r[0] != "6" and r[-2] != r[-1] and len(r) == 7:
        count += 1

print(count)
