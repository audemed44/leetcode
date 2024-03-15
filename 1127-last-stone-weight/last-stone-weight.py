class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*x for x in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            y = -1*heapq.heappop(stones)
            x = -1*heapq.heappop(stones)
            if x != y:
                y = y-x
                heapq.heappush(stones,-1*y)
        return -1*stones[0] if len(stones) == 1 else 0
        

        