class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for i in nums:
            if i in x:
                return True
            x[i] = 1
        return False
