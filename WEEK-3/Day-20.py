from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(map(str, range(1,10)))
        perm = ''
        k , factorial = k-1, 1
        for i in range(1, n):
            factorial *= i

        for i in range(n):
            index = k // factorial
            k = k % factorial
            factorial = factorial // (n-1-i) if n-1-i else 1
            perm += nums[index]
            del nums[index]
        return perm 