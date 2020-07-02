class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        low = 0
        high = len(citations)-1
        while low<=high:
            mid = (low + high)>>1
            if len(citations)-mid == citations[mid]:
                return citations[mid]
            elif citations[mid] > len(citations) - mid:
                high = mid-1
            else:
                low = mid+1
        return len(citations) - (high + 1)