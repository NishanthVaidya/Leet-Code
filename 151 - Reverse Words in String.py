class Solution:
    def reverseWords(self, s: str) -> str:
        onlyString = s.split()
        onlyString.reverse()
        return ' '.join(onlyString)
