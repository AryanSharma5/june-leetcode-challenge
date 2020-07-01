from bisect import bisect_left
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # First solution
        low = 0
        high = len(nums) - 1
        while low<=high:
            mid = (low + high)//2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low
        
        '''
        Second solution
        idx = -1
        for i in range(len(nums)):
            if target <= nums[i]:
                idx = i
                break
        if idx == -1:
            return len(nums)
        return idx'''
        
        
        '''
        Third solution
        idx = bisect_left(nums, target)
        if idx+1 < len(nums) and nums[idx+1] == target:
            return idx+1
        else:
            return idx'''