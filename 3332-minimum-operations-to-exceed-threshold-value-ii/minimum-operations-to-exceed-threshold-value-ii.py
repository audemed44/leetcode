class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0
        while nums[0]<k:
            min1, min2 = heapq.heappop(nums), heapq.heappop(nums)
            num = min(min1,min2)*2 + max(min1,min2)
            heapq.heappush(nums,num)
            operations += 1
        return operations

        