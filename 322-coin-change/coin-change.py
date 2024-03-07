class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(target,memo):
            if target == 0:
                return 0
            if target < 0:
                return float("inf")
            if target in memo:
                return memo[target]
            minCoins = float("inf")
            for i in coins:
                rem = target - i
                c = helper(rem,memo)
                if c != float("inf"):
                    minCoins = min(c+1,minCoins)
            memo[target] = minCoins
            return minCoins
        minC = helper(amount,{})
        return minC if minC != float("inf") else -1