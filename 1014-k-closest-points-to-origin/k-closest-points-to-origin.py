class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [(sqrt(point[0]*point[0]+point[1]*point[1]),[point[0],point[1]]) for point in points]
        heapq.heapify(res)
        ans = []
        while k>0:
            ans.append(heapq.heappop(res)[1])
            k -= 1
        return ans


        