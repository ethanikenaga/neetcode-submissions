class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        currentMin = prices[0]
        for i in range(1,len(prices)):
            if (prices[i] - currentMin) > 0:
                res = max(res, prices[i]-currentMin)
            currentMin = min(currentMin,prices[i])
        return res
        