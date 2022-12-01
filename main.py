if __name__ == '__main__':
    with open("diz.txt", "r", encoding="utf-8") as diz:
        data = "".join(diz.readlines()).split()
    print(len(data))
