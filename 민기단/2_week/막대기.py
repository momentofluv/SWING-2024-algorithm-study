#여러 줄을 입력받을 때는
#input()대신 sys.stdin.readline()을 사용 => 시간 초과 때문!!

#입출력 속도: sys.stdin.readline > raw_input() > input()

import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    stack.append(int(input()))

count = 0
bar = 0

for i in reversed(stack):
    if i > bar:
        count += 1
        bar = i

print(count)
