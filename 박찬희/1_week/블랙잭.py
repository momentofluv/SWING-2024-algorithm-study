n, max = map(int, input().split())  # 입력받은 값 두 변수에 나누어 정수형으로 저장
num = list(map(int, input().split()))   # 띄어쓰기 간격으로 입력된 값을 리스트로 저장
sum = 0
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = num[i] + num[j] + num[k]
            if ((sum <= max) and (sum > result)):   
                result = sum

print(result)
