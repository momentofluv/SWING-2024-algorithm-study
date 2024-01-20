from itertools import permutations

N, M = map(int, input().split())

def find(N, M):
    numbers = list(range(1, N + 1))
    sequences = permutations(numbers, M)

    for sequence in sequences:
        print(" ".join(map(str, sequence)))

find(N, M)
