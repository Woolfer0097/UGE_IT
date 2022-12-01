heap_limit = 29
turn = 1
for heap in range(-1, 30):
    count = 0
    while heap < heap_limit:
        if 0 < heap * 2 >= heap_limit:
            heap += 1
        else:
            heap *= 2
        turn = 1 if turn == 2 else 2
        count += 1
if count == 1:
    if turn == 1:
        print(heap)
