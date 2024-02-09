class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for i in s:
            if s_map.get(i) is None:
                s_map[i] = 1
            else:
                s_map[i] += 1
        for i in t:
            if t_map.get(i) is None:
                t_map[i] = 1
            else:
                t_map[i] += 1
        return s_map == t_map
            

        