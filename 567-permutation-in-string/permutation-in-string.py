class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map1 = defaultdict(int)
        for i in s1:
            freq_map1[i] += 1
        for l in range(len(s2)-len(s1)+1):
            freq_map2 = defaultdict(int)
            for r in range(len(s1)):
                freq_map2[s2[l+r]] += 1
            if freq_map1==freq_map2:
                return True
        return False
        
        return False

            


        