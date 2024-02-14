class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        res = [0]*len(nums)
        for i in nums:
            if i >= 0:
                positive.append(i)
            else:
                negative.append(i)
        p,n=0,0
        for i in range(len(nums)):
            if i%2==0 or i==0:
                res[i]=positive[p]
                p += 1
            else:
                res[i] = negative[n]
                n += 1
        return res
        