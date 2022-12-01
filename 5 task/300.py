result = []

for n in range(2, 1000):
    number = bin(n).replace("0b", "")
    number = number[1:]
    if number.count("1") % 2 == 0:
        number = f"10{number}"
    else:
        number = f"1{number}0"
    if int(number, 2) < 450:
        result.append(int(number, 2))

print(max(result))
