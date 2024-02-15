class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i] += prefix_sum[i-1]+nums[i]
        i = len(nums)-1
        while i>=2:
            if prefix_sum[i-1] > nums[i]:
                return prefix_sum[i-1]+nums[i]
            i -= 1
        return -1

