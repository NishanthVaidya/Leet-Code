#Approach 1

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

#Approach 2
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
