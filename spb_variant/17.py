data = list(map(int, open("17.txt").readlines()))

r = []
maxim = max([i**2 for i in data if str(i)[-1] == "5"])
for i in range(len(data) - 1):
    p1 = data[i]
    p2 = data[i + 1]
    if str(p1)[-1] == "5" and str(p2)[-1] != "5" or str(p1)[-1] != "5" and str(p2)[-1] == "5" and\
       abs(p1**2 - p2**2) <= maxim:
        r.append(abs(p1**2 - p2**2))


print(len(r), max(r))
