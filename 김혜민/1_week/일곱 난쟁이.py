n = [0] * 9
for i in range(9):
    n[i] = int(input())

def find(n):
    for i in range(8):
        for j in range(i + 1, 9):
            if sum(n) - (n[i] + n[j]) == 100:
                real = [n[k] for k in range(9) if k != i and k != j]
                real.sort()
                print(*real)
                return
find(n)
