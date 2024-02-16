class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        sorted_cnt = sorted(cnt.items(), key= lambda x: x[1])
        for key, val in sorted_cnt:
            if k >= val:
                del cnt[key]
                k -= val
            else:
                break
        return len(cnt)