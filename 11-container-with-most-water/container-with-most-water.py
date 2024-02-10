class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        while r > l:
            if height[l] < height[r]:
                res = max(res,(r-l)*height[l])
                l += 1
            else:
                res = max(res,(r-l)*height[r])
                r -= 1
        return res
        