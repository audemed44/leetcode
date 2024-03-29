class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_elem = max(nums)
        index_max_elem = []
        res = 0

        for index, element in enumerate(nums):
            if element == max_elem:
                index_max_elem.append(index)
            
            freq = len(index_max_elem)
            if freq >= k:
                res += index_max_elem[-k] + 1
        return res
        