# 0/1 knapsack problem 

weight = [2, 3, 4]
values= [200, 300, 500]

capacity=4
n = len(weight)
dp = [[0] * (capacity + 1) for i in range(n+1)]

for i in range (1, n+1) :
    for w in range (1, capacity+1):

        if weight[i-1] <=w :
            take = values[i-1] + dp[ i-1][w-weight[i-1]]
            not_take= dp[i-1][w]
            dp[i][w] = max(take, not_take)
        else:
            dp[i][w]= dp[i-1][w]

print("maximum value = ", dp[n][capacity])