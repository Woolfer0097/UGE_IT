result = []

with open("data/17 (36).txt") as f:
    data = [int(i) for i in f.readlines()]
    min_even_element = min([i for i in data if i % 2 == 0])
    for i in range(len(data) - 1):
        p1 = data[i]
        p2 = data[i + 1]
        if (p1 % 3 == 0 and p2 % 3 != 0) or (p1 % 3 != 0 and p2 % 3 == 0) and \
                abs(p1 - p2) < min_even_element:
            result.append(abs(p1 - p2))


print(len(result), max(result))
