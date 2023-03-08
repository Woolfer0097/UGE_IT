maximal = 0

with open("27data/124/27-124a.txt", "r") as f:
    n, k, v, m = map(int, f.readline().split())
    for _ in range(n):
        km, w = map(int, f.readline())
        
        if res > maximal:
            maximal = res