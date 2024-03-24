def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount -= coin * (amount // coin)
    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    used_coins = {}
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = coin
    result = {}
    while amount > 0:
        coin = used_coins[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    return result

# Приклад використання функцій:
amount = 113
print("Жадібний алгоритм:", find_coins_greedy(amount))
print("Динамічне програмування:", find_min_coins(amount))