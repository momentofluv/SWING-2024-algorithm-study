N,B = input().split(" ")
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = N[::-1]
result = 0

#enumerate 함수를 통해서 각 인덱스(i)와 값(n)을 받아옴
for i,n in enumerate(N):
    result += (int(B)**i)*(number.index(n))
print(result)
