class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(cur, dp={}):
            if cur < 0: 
                return 0
            if cur == 0:
                return nums[0]
            if cur in dp:
                return dp[cur]
            dp[cur] = max(helper(cur-2)+nums[cur],helper(cur-1))
            return dp[cur]
        return helper(len(nums)-1)