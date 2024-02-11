class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l,r=0,1
        while r < len(prices) and l < len(prices)-1:
            currp = prices[r]-prices[l]
            if currp > 0:
                maxp = max(currp,maxp)
                r += 1
            else:
                l += 1
                if l == r:
                    r += 1
        return maxp
