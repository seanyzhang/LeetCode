class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [0] * (amount + 1)
        dp[0] = 0

        for i in range(1,amount + 1):
            minCoins = float('inf')
            for coin in coins:
                diff = i - coin 
                if diff < 0: 
                    break
                minCoins = min(minCoins, 1 + dp[diff])
            dp[i] = minCoins

        return dp[amount] if dp[amount] < float('inf') else -1
                


