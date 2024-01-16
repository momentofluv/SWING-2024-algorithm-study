height = []
false_a = 0
false_b = 0

for i in range(9):
    x = int(input())
    height.append(x)

total = sum(height)

for i in range(9):
    for j in range(i+1, 9):     # i와 j가 같아서는 안 됨
        if total - (height[i] + height[j]) == 100:
            false_a = height[i]
            false_b = height[j]

height.remove(false_a)
height.remove(false_b)
height.sort()

for i in range(7):
    print(height[i])

# from itertools import combinations

# height = []
# answer = []

# for i in range(9):
#     x = int(input())
#     height.append(x)

# real = list(combinations(height, 7))

# for i in real:
#     if sum(i) == 100:
#         answer = list(i)
#         break

# answer.sort()

# for i in range(7):
#      print(answer[i])