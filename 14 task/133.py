def transfer_x_to_2(number, base):
    result = []
    dvuad = {'0': "00", '1': "01", '2': "10", '3': "11"}
    triad = {'0': "000", '1': "001", '2': "010", '3': "011",
             '4': "100", '5': "101", '6': "110", '7': "111"}
    tetrad = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
              '4': "0100", '5': "0101", '6': "0110", '7': "0111",
              '8': "1000", '9': "1001", '10': "1010", '11': "1011",
              '12': "1100", '13': "1101", '14': "1110", '15': "1111"}
    base_links = {4: dvuad, 8: triad, 16: tetrad}
    for i, digit in enumerate(list(str(number))):
        if digit in base_links[base].keys():
            result.append(base_links[base][digit].zfill(4))
        else:
            result.append(digit * 4)
    return "".join(result)


print(transfer_x_to_2("***", 16))
print(transfer_x_to_2("4*2", 8))
