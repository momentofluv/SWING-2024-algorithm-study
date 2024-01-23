import sys

input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    stack.append(int(input()))

last = stack[-1]
cnt = 1

for i in reversed(range(N)):
    if stack[i] > last:
        cnt += 1
        last = stack[i]

print(cnt)