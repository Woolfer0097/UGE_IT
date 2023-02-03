res = []
with open("17/17var13.txt", "r", encoding="utf-8") as f:
    data = list(map(int, f.readlines()))
    for i in range(len(data) - 1):
        current_elem = data[i]
        next_elem = data[i + 1]
        if current_elem + next_elem >= 100 and (current_elem < 0 or next_elem < 0):
            res.append(current_elem * next_elem)

print(len(res), max(res))
