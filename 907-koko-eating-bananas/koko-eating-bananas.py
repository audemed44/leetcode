class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def verify(speed):
            total = 0
            for i in piles:
                total += math.ceil(i/speed)
            return total
        
        l,r=1,max(piles)
        min_speed = r
        while r >= l:
            speed = (l+r)//2
            hours = verify(speed)
            if hours <= h:
                min_speed = min(min_speed,speed)
                r = speed - 1
            else:
                l = speed + 1
        return min_speed

        