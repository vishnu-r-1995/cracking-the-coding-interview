class CoinChange(object):
    def coinChange(self, coins, amount):
        #Solution for coins = [1,2,5]
        coins = [1,2,5]
        dp = []
        dp.insert(0, 0)
        dp.insert(1, 1)
        for i in range(2, amount + 1):
            if i in coins:
                dp.insert(i, 1)
            else:
                if (i < 6):
                    dp.insert(i, min(dp[i-1] + dp[1], dp[i-2] + dp[2]))
                else:
                    dp.insert(i, min(dp[i-1] + dp[1], dp[i-2] + dp[2], dp[i-5] + dp[5]))
        return dp[amount]    
