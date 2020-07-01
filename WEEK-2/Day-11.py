class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Using Extra Space
        count = [0, 0]
        for i in nums:
            curr = nums.pop()
            if curr == 0:
                nums.insert(0,0)
                count[0] += 1
            elif curr == 1:
                nums.insert(count[0], 1)
                count[1] += 1
            else:
                nums.insert(count[0] + count[1], 2)
        return nums'''
        
        i = j = k = -1
        for p in range(len(nums)):
            if nums[p] == 2:
                k += 1
                nums[k] = 2
            elif nums[p] == 1:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1
            else:
                k += 1
                nums[k] = 2
                j += 1
                nums[j] = 1
                i += 1
                nums[i] = 0
        return nums