class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set('aeiou')
        reqv = False
        reqc = False
        
        if len(word) < 3:
            return False
        
        for ch in word:
            if not (ch.isalpha() or ch.isdigit()):
                return False
        
        for ch in word.lower():
            if ch.isalpha():
                if ch in vowels:
                    reqv = True
                else:
                    reqc = True
            if reqv and reqc:
                return True
        
        return False
