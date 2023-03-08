with open("26data/26-k1.txt", "r") as f:
    d = f.readlines()
    n, k = map(int, d[0].split())
    data = list(map(int, d[1:]))


discount_sum = 0
data.sort(reverse=True)
for i in range(k):
    discount_sum += data[i] * 0.2
    data[i] *= 0.2


print(max(data[k:n]), int(discount_sum))
