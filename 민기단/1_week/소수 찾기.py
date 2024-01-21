n = int(input())
num = list(map(int, input().split()))
result = 0

for n in num:
    count = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                count += 1
        
        if count == 0:
            result += 1
    
print(result)
