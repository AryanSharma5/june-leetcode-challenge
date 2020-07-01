from collections import defaultdict
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def findLargest(arr, n): 
            arr.sort(reverse = False) 
            divCount = [1 for i in range(n)] 
            prev = [-1 for i in range(n)] 
            max_ind = 0
            for i in range(1,n): 
                for j in range(i): 
                    if (arr[i] % arr[j] == 0): 
                        if (divCount[i] < divCount[j] + 1): 
                            divCount[i] = divCount[j]+1
                            prev[i] = j 
                if (divCount[max_ind] < divCount[i]): 
                    max_ind = i 
            k = max_ind 
            ans = []
            while (k >= 0): 
                ans.append(arr[k]) 
                k = prev[k]
            return ans
        if not nums:
            return []
        return findLargest(nums, len(nums))