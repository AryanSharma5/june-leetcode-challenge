class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        thresh = len(costs)//2
        costs.sort(key = lambda x : x[0] - x[1])
        ans = sum([cost[0] for cost in costs[:thresh]]) + sum([cost[1] for cost in costs[thresh:]])
        return ans