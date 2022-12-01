rangement = range(150, 250)

count = 0
for n in range(2, 100):
    result = ""
    number = bin(n).replace("0b", "")
    result += number
    result += number[-2]
    result += number[1]
    if int(result, 2) in rangement:
        count += 1

print(count)
