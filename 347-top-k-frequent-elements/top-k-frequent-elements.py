class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for i in nums:
            freq_map[i] += 1
        result=[x[0] for x in sorted(freq_map.items(),key= lambda x: x[1], reverse=True)]
        return result[:k]