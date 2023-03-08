with open("26data/26-k3.txt", "r") as f:
    d = f.readlines()
    n, k, m = map(int, d[0].split())
    data = list(map(int, d[1:]))


# k - победители, m - призёры
data.sort(reverse=True)

print(min(data[k:k + m]), min(data[:k]))
# k:k + m потому что [1, 2, 3, 4, 5], если k = 1, m = 3, то k [1], а m = [k:k+m]([1:1+3]) = [2, 3, 4]
