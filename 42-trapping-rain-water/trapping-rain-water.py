class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_left = height[l]
        max_right = height[r]
        water_sum = 0
        while r > l:
            if max_left < max_right:
                if max_left - height[l] > 0:
                    water_sum += max_left-height[l]
                l += 1
                max_left = max(max_left, height[l])
            else:
                if max_right - height[r] > 0:
                    water_sum += max_right-height[r]
                r -= 1
                max_right = max(max_right,height[r])
        return water_sum

        