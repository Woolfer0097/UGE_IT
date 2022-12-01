expression = 6 ** 1333 - 5 * 6 ** 1215 + 3 * 6 ** 144 - 86
BASE = 6


def transfer_10_to_x(number, base):
    result = []
    while number > base:
        rest = number % base
        result.append(rest)
        number //= base
    return result[::-1]


print(sum(transfer_10_to_x(expression, BASE)))
