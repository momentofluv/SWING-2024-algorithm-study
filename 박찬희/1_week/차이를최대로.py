from itertools import permutations
n = int(input())
num = list(map(int, input().split()))
sum = 0
temp = 0

for i in permutations(num):         # num으로 조합할 수 있는 모든 순열 생성
    temp = 0
    for j in range(n-1):
        temp += abs(i[j] - i[j+1])  # i가 순열로 새롭게 순서가 변경된 리스트임

    if (sum < temp):
        sum = temp


print(sum)

