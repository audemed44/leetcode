class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = defaultdict(list)
        for s in strs:
            result_map[tuple(sorted(s))].append(s)
        return [x for x in result_map.values()]
            

   