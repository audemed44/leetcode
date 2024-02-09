class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_set = set(nums)
        count_max = 0
        for i in nums:
            if i-1 not in seq_set:
                count = 1
                j = i
                while j+1 in seq_set:
                        count += 1
                        j += 1
                if count > count_max:
                    count_max = count
        return count_max