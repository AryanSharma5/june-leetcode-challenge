import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.ls = []
        for ele in w:
            if self.ls:
                self.ls.append(self.ls[-1] + ele)
            else:
                self.ls.append(ele)

    def pickIndex(self) -> int:
        r = random.randint(0, self.ls[-1]-1)
        return bisect.bisect_right(self.ls, r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()