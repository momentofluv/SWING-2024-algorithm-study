n = int(input())
nums = list(map(int, input().split()))
result = 0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in nums:
    if is_prime(num):
        result += 1

print(result)
