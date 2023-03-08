def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


for b in range(2, 512):
    for a in range(2, 512):
        if convert_to(165, a) == convert_to(341, b):
            print(a)
            break
