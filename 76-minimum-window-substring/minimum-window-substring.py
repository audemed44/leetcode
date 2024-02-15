class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        l = 0
        minL,minR=-1,-1
        freq_s=defaultdict(int)
        minW = float("infinity")
        have,need = 0,len(freq_t)
        for r in range(len(s)):
            ch = s[r]
            freq_s[ch] += 1
            if ch in freq_t and freq_s[ch] == freq_t[ch]:
                have += 1
            while have==need:
                if (r-l+1) < minW:
                    minL,minR = l,r+1
                    minW = r-l+1
                freq_s[s[l]] -= 1
                if s[l] in freq_t and freq_t[s[l]] > freq_s[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return "" if minL==-1 else s[minL:minR]
        