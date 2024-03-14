class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_num = 0
        count = Counter({0:1})
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            total_num += count[current_sum-goal]
            count[current_sum] += 1
        return total_num