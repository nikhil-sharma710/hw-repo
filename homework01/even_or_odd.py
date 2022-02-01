import random

list = []

i = 0

while (i < 10):
    list.append(random.randint(0, 100))
    i = i + 1

i = 0

while (i < 10):
    print(list[i])
    if (list[i]%2 == 0):
        print('even')
    else:
        print('odd')
    i = i + 1
