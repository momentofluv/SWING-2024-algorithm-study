L = int(input())
string = input().rstrip()
answer = 0
r = 31
M = 1234567891

for i, char in enumerate(string):
    answer += (ord(char) - ord('a') + 1) * (r ** i)

print(answer % M)
