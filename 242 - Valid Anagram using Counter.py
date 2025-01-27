class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False
        else:
            if(Counter(s) != Counter(t)):
                return False
        return True
