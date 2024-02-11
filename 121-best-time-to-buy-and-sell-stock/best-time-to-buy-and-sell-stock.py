class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxP = 0
        while r < len(prices):
            currP = prices[r] - prices[l]
            if currP > 0:
                maxP = max(maxP,currP)
            else:
                l = r
            r += 1
        return maxP
        