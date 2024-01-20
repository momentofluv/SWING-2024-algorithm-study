num = int(input())
cash = []
# q = 25 d = 10 n = 5 p = 1

for i in range(num):
    coin_q = coin_d = coin_n = coin_p = 0
    m = int(input())
    cash.append(m)

    coin_q = int(cash[i] / 25)
    cash[i] = cash[i] - coin_q * 25

    coin_d = int(cash[i] / 10)
    cash[i] %= 10

    coin_n = int(cash[i] / 5)
    cash[i] = cash[i] - coin_n * 5

    coin_p = cash[i]

    print(str(coin_q)+" "+str(coin_d)+" "+str(coin_n)+" "+str(coin_p))