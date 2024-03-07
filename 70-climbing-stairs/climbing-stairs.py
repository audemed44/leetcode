class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(num,memo={}):
            if num == 1:
                return 1
            if num == 2:
                return 2
            if num in memo:
                return memo[num]
            memo[num] = helper(num-1,memo) + helper(num-2,memo)
            return memo[num]
        return helper(n)