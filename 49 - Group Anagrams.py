from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hasher = defaultdict(list)
        result = []

        for each in strs:
            sorted_s = tuple(sorted(each))
            hasher[sorted_s].append(each)
        
        for each in hasher.values():
            result.append(each)

        return result
