N, M = map(int, input().split())
card = list(map(int, input().split()))

max = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            sum = card[i] + card[j] + card[k]
            if sum <= M and sum > max:
                max = sum
print(max)
