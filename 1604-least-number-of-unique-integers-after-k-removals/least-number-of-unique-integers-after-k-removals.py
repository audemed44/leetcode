class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        deleted_count = 0
        sorted_cnt = sorted(cnt.items(), key= lambda x: x[1])
        for key, val in sorted_cnt:
            if k >= val:
                deleted_count += 1
                k -= val
            else:
                break
        return len(cnt)-deleted_count