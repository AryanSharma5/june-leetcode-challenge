class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_ele_sum = sum(set(nums))
        return (3*unique_ele_sum - sum(nums))//2