class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns = s + t
        left = 0
        right = len(s)
        if(s == ""):
            return True
        while(right < len(ns)):
            if(ns[left] != ns[right]):
                right += 1
            else:
                left += 1
                right += 1
            if(left == len(s)):
                return True
        return False
        
