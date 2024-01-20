from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

# 주어진 배열의 모든 순열을 생성
permu = list(permutations(arr, n))

def calculator(li):
    total = 0
    for i in range(len(li) - 1):
        total += abs(li[i] - li[i + 1])
    return total

#answer 변수를 매우 작은 값으로 초기화: -1e9
answer = 0
for li in permu:
    answer = max(answer, calculator(li))

print(answer)
