class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            d = 1
            total = 0
            for w in weights:
                total += w
                if total > capacity:
                    total = w
                    d += 1
                    if d > days:
                        return False
            return True
        left = max(weights)
        right = sum(weights)
        while right > left:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        