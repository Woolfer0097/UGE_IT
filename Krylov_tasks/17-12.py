result = []


with open("17/17var12.txt", "r") as file:
    data = list(map(int, file.readlines()))
    for i in range(len(data) - 1):
        current_element = data[i]
        next_element = data[i + 1]
        if int(str(current_element)[-1]) % 2 != 0 and \
                int(str(next_element)[-1]) % 2 != 0 and \
                int(str(current_element)[-1]) % 2 != int(str(next_element)[-1]):
            result.append(abs(current_element) * abs(next_element))


print(len(result), min(result))
