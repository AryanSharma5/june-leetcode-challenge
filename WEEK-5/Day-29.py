from functools import lru_cache
import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''@lru_cache(maxsize = 1024)
        def ans(m, n):
            if m==1 or n==1:
                return 1
            return ans(m-1, n) + ans(m, n-1)
        return ans(m, n)'''
        
        def ans(m, n):
            dp = [[0 for i in range(m)] for j in range(n)]
            for i in range(m):
                dp[0][i] = 1
            for j in range(n):
                dp[j][0] = 1
            for i in range(1, n):
                for j in range(1, m):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
            print(np.array(dp))
            return dp[n-1][m-1]
        return ans(m, n)