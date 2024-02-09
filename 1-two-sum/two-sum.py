class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}
        for idx,i in enumerate(nums):
            req = target - i
            if req in target_map:
                return [idx,target_map[req]]
            target_map[i] = idx
            

             

        