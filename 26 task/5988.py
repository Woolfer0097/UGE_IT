with open("26_5988.txt", "r") as f:
    data = {"R": [], "G": [], "B": []}
    n = f.readline()
    for _ in range(n):
        length, color = f.readline().split()
        data[color].append(length)

