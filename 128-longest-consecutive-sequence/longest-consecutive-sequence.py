class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq_set = set()
        count_max = 0
        for idx,i in enumerate(nums):
            seq_set.add(i)
        for idx, i in enumerate(nums):
            if i-1 not in seq_set:
                count = 1
                j = i
                while j+1 in seq_set:
                        count += 1
                        j += 1
                if count > count_max:
                    count_max = count
        return count_max