from gintonic import use_memo

from gintonic import timer
import matplotlib.pyplot as plt


def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])

    optimal = []
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] > dp[i - 1][j]:
            optimal.append(i - 1)
            j -= weights[i - 1]

    return dp[n][capacity], optimal[::-1]


weights = [20, 10, 12, 7, 7, 10, 12, 16, 9, 7, 13, 10, 9, 8, 15, 20, 13, 17]
prices = [3, 4, 5, 2, 3, 4, 3, 5, 1, 3, 4, 2, 1, 5, 3, 5, 4, 4]
c = 30

knapsack_memo = use_memo(knapsack)
five = knapsack(weights[0:5], prices[0:5], c)
ten = knapsack(weights[0:10], prices[0:10], c)
fifteen = knapsack(weights[0:15], prices[0:15], c)
seventeen = knapsack(weights, prices, c)
print("5 вещей: ", five)
print("Стоимость: ", five[0])
print("Индексы элементов: ", five[1])
print()
print("10 вещей: ", ten)
print("Стоимость: ", ten[0])
print("Индексы элементов: ", ten[1])
print()
print("15 вещей: ", fifteen)
print("Стоимость: ", fifteen[0])
print("Индексы элементов: ", fifteen[1])
print()
print("17 вещей: ", seventeen)
print("Стоимость: ", seventeen[0])
print("Индексы элементов: ", seventeen[1])

times = []
times.append(timer(knapsack_memo, weights[0:5], prices[0:5], c))
times.append(timer(knapsack_memo, weights[0:10], prices[0:10], c))
times.append(timer(knapsack_memo, weights[0:15], prices[0:15], c))
times.append(timer(knapsack_memo, weights, prices, c))

times_memo = []
times_memo.append(timer(knapsack_memo, weights[0:5], prices[0:5], c))
times_memo.append(timer(knapsack_memo, weights[0:10], prices[0:10], c))
times_memo.append(timer(knapsack_memo, weights[0:15], prices[0:15], c))
times_memo.append(timer(knapsack_memo, weights, prices, c))

x = [5, 10, 15, 17]
plt.figure(1)
plt.plot(x, times)
plt.title("Без мемоизации")
plt.grid()

plt.figure(2)
plt.plot(x, times_memo)
plt.title("Используя мемоизацию")
plt.grid()
plt.show()
