class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        rob_a, rob_b = nums[0], max(nums[0],nums[1])
        for i in range(2,len(nums)):
            rob_a, rob_b = rob_b, max(rob_a + nums[i],rob_b)
        return rob_b
