class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_map = {}
        sum_val = 0
        max_len = 0
        for index, num in enumerate(nums):
            if num == 0:
                sum_val -= 1
            else:
                sum_val += 1
            if sum_val == 0:
                max_len = index + 1
            elif sum_val in sum_map:
                max_len = max(max_len, index - sum_map[sum_val])
            else:
                sum_map[sum_val] = index
        return max_len
        