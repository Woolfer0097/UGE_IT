with open("27/27v12_A.txt", "r", encoding="utf-8") as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file.readlines()[1:]]

result = []

while True:
    for j in range(n - 1):
        result.append(max(data[j]))
    if sum(result) % 37 != 0:
        print(sum(result))
        break
    result.pop(-1)
