money = int(input())
coins = [1, 3, 4]
def money_changer(money, coins):
    minnumcoins = [0] * (money + 1)
    for m in range(1, money + 1):
        minnumcoins[m] = float('inf')
        for coin in range(0, len(coins)):
            if m >= coins[coin]:
                numcoins = minnumcoins[m - coins[coin]] + 1
                if numcoins < minnumcoins[m]:
                    minnumcoins[m] = numcoins
    return minnumcoins[money]

print(money_changer(money, coins))