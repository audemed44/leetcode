class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def matches(substr_map,freq_map):
            for i in substr_map:
                if i in freq_map and freq_map[i] >= substr_map[i]:
                    continue
                else:
                    return False
            return True

        freq_t = Counter(t)
        l = 0
        minL,minR=-1,-1
        freq_s=defaultdict(int)
        minW = float("infinity")
        for r in range(len(s)):
            freq_s[s[r]] += 1
            while matches(freq_t,freq_s):
                if (r-l+1) < minW:
                    minL,minR = l,r+1
                    minW = r-l+1
                freq_s[s[l]] -= 1
                l += 1
            r += 1
        return "" if minL==-1 else s[minL:minR]
        