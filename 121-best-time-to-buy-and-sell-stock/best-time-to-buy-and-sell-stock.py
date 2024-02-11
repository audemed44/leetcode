class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l,r=0,1
        while r < len(prices):
            currp = prices[r]-prices[l]
            if currp > 0:
                maxp = max(currp,maxp)
            else:
                l = r
            r += 1
        return maxp
