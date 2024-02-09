class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]*(len(nums))
        right_product = [1]*(len(nums))
        result = []
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            left_product[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            right_product[i] = postfix
            postfix *= nums[i]
        for i in range(len(nums)):
            result.append(left_product[i]*right_product[i])
        return result
            
        