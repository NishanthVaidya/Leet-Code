class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        li = []
        res = ""
        for i in range(len(s)):
            if s[i].lower() in vowels:
                li.append(s[i])
        for i in range(len(s)):
            if s[i].lower() in vowels:
                res += li.pop()
            else:
                res += s[i]
        return res
