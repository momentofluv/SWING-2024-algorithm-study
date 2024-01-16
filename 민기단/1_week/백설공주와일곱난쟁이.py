array = []
for i in range(9):
    array.append(int(input()))
total = sum(array)

for i in range(9):
    for j in range(i + 1, 9):
        if total - array[i] - array[j] == 100:
            a,b=i,j
            break
array.pop(a)
array.pop(b-1)
for i in array:
    print(i)