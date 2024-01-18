# n = int(input())
# number = list(map(int, input().split()))
# answer = n

# for i in range(n):
#     if number[i] == 1:
#         answer -= 1
#     else:
#         for j in range(2, number[i]):
#             if number[i] % j == 0: 
#                 answer -= 1
#                 break

# print(answer) 

n = int(input())
number = list(map(int, input().split()))
answer = 0

for i in number:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
        	    answer += 1
            break

print(answer)