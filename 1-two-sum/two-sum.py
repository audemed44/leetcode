class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}
        for idx,i in enumerate(nums):
            target_map[i] = idx
        for idx,i in enumerate(nums):
            if target-i in target_map and target_map[target-i] != idx:
                return [idx, target_map[target-i]]
        return []
            

             

        