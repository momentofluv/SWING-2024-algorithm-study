import sys
input = sys.stdin.readline

def reverse_word(word):
    return word[::-1]

string = input().rstrip()
tag = False
res = ''
word = ''

for i in string:
    if i == " ":
        res += reverse_word(word)
        res += i
        word = ''
    elif i == "<":
        res += reverse_word(word)
        tag = True
        res += i
        word = ''
    elif i == ">":
        tag = False
        res += i
    elif tag:
        res += i
    else:
        word += i

res += reverse_word(word)
print(res)
