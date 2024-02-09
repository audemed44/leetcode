class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, i in enumerate(nums):
            if idx > 0 and i == nums[idx-1]:
                continue
            l = idx+1
            r = len(nums)-1
            while r>l:
                threesum = i+nums[l]+nums[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([i,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and r>l:
                        l += 1
        return res

        