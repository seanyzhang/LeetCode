class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [[float('inf') for j in range(amount + 1)] for i in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            dp[i][0] = 0

        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(
                        dp[i-1][j], 
                        1 + dp[i][j - coins[i - 1]]
                        )
        
        result = dp[len(coins)][amount]
        return result if result != float('inf') else -1
