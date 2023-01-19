data = []

with open("26/26var12.txt", "r", encoding="utf-8") as file:
    S, N = map(int, file.readline().split())
    for i in file.readlines()[1:]:
        data.append(int(i))

data.sort()
prev_file_size = 0
result = []

while True:
    for j in range(len(data)):
        file_size = data.pop(j)
        if S - file_size > 0:
            S -= file_size
            result.append(file_size)
            prev_file_size = file_size
        elif S - file_size == 0:
            print(len(set(result)), max(set(result)))
            break
        else:
            S += prev_file_size
            result.pop(-1)
    break
