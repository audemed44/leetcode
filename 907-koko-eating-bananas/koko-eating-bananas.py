class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def verify(speed):
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i]/speed)
            return total

        l,r=1,max(piles)
        min_speed = r
        while r >= l:
            speed = (l + r)//2
            hours = verify(speed)
            if hours <= h:
                min_speed = min(speed,min_speed)
                r = speed-1
            else:
                l = speed+1
        return min_speed
                
        