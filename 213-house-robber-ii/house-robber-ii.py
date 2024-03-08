class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        rob_a, rob_b = nums[0], max(nums[0],nums[1])
        for i in range(2,n-1):
            rob_a, rob_b = rob_b, max(rob_a+nums[i],rob_b)
        max1 = rob_b
        rob_a, rob_b = nums[1],max(nums[1],nums[2])
        for i in range(3,n):
            rob_a, rob_b = rob_b, max(rob_a+nums[i],rob_b)
        return max(rob_b,max1)
        
        