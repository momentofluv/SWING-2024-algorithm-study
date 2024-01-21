def backtracking(start):
    if len(array) == m:
        print(' '.join(map(str, array)))
        return
    
    for i in range(start, n+1):
        array.append(i)
        backtracking(i)
        array.pop()

n,m = map(int, input().split())
array=[]

backtracking(1)