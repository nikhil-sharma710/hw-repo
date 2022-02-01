for i in range(3, 100):
    for j in range(2, i):
        if (i % j != 0):
            continue
        else:
            break
    if (j == i - 1):
        print(i)
