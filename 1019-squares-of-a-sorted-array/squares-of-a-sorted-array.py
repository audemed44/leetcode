class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = i = len(nums) - 1
        ans = [0] * len(nums)
        while r >= l:
            if abs(nums[l]) > abs(nums[r]):
                ans[i] = nums[l]*nums[l]
                l += 1
            else:
                ans[i] = nums[r]*nums[r]
                r -= 1
            i -= 1
        return ans
        