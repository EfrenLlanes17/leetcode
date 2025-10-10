from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)
        for s in strs:
            anaMap[tuple(sorted(s))].append(s)
        return list(anaMap.values())
