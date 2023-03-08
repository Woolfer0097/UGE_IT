with open("26data/26-k2.txt", "r") as f:
    d = f.readlines()
    n, k = map(int, d[0].split())
    data = list(map(int, d[1:]))


data.sort()
true_measures = data[k:n - k]

print(max(true_measures), int(sum(true_measures) / len(true_measures)))
