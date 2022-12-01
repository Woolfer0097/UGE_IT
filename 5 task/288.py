result = set()
for i in range(2, 200):
    number = bin(i).replace("0b", "")
    if number[-1] == "0":
        number = f"1{number}10"
    elif number[-1] == "1":
        number = f"11{number}0"
    if 800 <= int(number, 2) <= 1500:
        result.add(int(number, 2))

print(len(result))
