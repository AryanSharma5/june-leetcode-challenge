import math
class Solution:
    def numTrees(self, n: int) -> int:
        p = 2*n
        r = n
        x = math.factorial(p)//(math.factorial(n)*math.factorial(p-n))
        return x//(n+1)