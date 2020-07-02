class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = max(nums)
        return sum(nums) - (n*(n+1))//2