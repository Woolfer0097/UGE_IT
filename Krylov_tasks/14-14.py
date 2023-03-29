numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]

result = []
for x in numbers:
    n1 = f"135{x}9 task"
    n2 = f"9 task{x}531"
    expression = int(n1, 17) + int(n2, 17)
    if expression % 9 == 0:
        result.append([int(x, 17), expression])

result.sort(key=lambda y: y[0])
print(result[-1][1] // result[-1][0])
