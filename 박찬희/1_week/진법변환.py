number, b = input().split()
number = number[::-1]   # 슬라이싱으로 문자열 순서 변경
b = int(b)
answer = 0

num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(number)-1, -1, -1): #[::-1]도 동일
    answer += num_list.index(number[i]) * (b**i)

print(answer)