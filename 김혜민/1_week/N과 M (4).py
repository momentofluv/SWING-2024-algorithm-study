from itertools import combinations_with_replacement

N, M = map(int, input().split())

def find(N, M):
    numbers = list(range(1, N + 1))
    sequences = combinations_with_replacement(numbers, M)

    for sequence in sequences:
        print(" ".join(map(str, sequence)))


find(N, M)
