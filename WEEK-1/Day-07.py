#import numpy as np
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for i in range(amount + 1)] for j in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                x = dp[i-1][j]
                y = dp[i][j - coins[i - 1]] if j - coins[i - 1] >= 0 else 0
                dp[i][j] = x + y
        #print(np.array(dp))
        return dp[len(coins)][amount]