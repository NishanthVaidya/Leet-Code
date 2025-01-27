class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False
        else:
            sorted_s = sorted(s)
            sorted_t = sorted(t)
            for i in range(len(sorted_s)):
                if sorted_s[i] != sorted_t[i]:
                    return False
        return True
        
