T = int(input())

for _ in range(T):
    money = int(input())
    for coin in [25, 10, 5, 1]:
        count = money // coin
        print(count, end=' ')
        money = money % coin
    print()