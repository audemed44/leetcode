class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_cnt = 0
        max_freq = 0
        freq_counter = defaultdict(int)
        for i in nums:
            freq_counter[i] += 1
            if freq_counter[i] > max_freq:
                max_freq = freq_counter[i]
                max_cnt = 1
            elif freq_counter[i] == max_freq:
                max_cnt += 1
        return max_cnt * max_freq