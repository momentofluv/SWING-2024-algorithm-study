array = []
for i in range(9):
    array.append(int(input()))

array.sort()
total = sum(array)

for i in range(9):
    for j in range(i + 1, 9):
        if total - array[i] - array[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    pass
                else:
                    print(array[k])
            exit()