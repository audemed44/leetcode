class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_map = defaultdict(int)
        for i in s:
           freq_map[i] += 1
        for i in t:
            freq_map[i] -= 1
        return all(x == 0 for x in freq_map.values())
            

        