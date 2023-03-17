from math import ceil


def get_nearest_value(iterable, value):
    return min(iterable, key=lambda x: abs(x - value))


d = {}
m_n = -10 ** 10
s = 0
with open("27_A.txt", "r") as f:
    n = int(f.readline())
    for _ in range(n):
        index, number = map(int, f.readline().split())
        d[index] = number
        if number > m_n:
            m_n = number


m_n_i = [i for i, p in d.items() if p == m_n]
m_n_p = [p for i, p in d.items() if p == m_n]
m_i = get_nearest_value(m_n_i, sum(m_n_i) / len(m_n_i))

res = 0
for i, p in d.items():
    res += abs(m_i - i) * ceil(p / 48)


print(res)
