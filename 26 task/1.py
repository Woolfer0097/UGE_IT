with open("26data/26.txt", "r") as f:
    a = f.readlines()
    s, n = map(int, a[0].split())
    data = list(map(int, a[1:]))


data.sort()
c = []
for i in data:
    if sum(c) + i > s:
        break
    else:
        c.append(i)

for i in data[::-1]:
    if sum(c) - c[-1] + i <= s:
        print(len(c), i)
        break
