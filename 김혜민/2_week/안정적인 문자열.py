answer = []
test_case = 0

while True:
    stack = []
    cnt = 0
    s = input().rstrip()
    if '-' in s:
        break
    
    test_case += 1
    
    for bracket in s:
        if not stack and bracket == '}':
            cnt += 1
            stack.append('{')
        elif stack and bracket == '}':
            stack.pop()
        else:
            stack.append(bracket)
    
    cnt += len(stack) // 2
    answer.append(cnt)

for i, cnt in enumerate(answer, start=1):
    print(f"{i}. {cnt}")
