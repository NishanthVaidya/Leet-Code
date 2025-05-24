class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = s.strip()
        count = 0
        for each in range(len(strs) -1, -1, -1):
            if (strs[each]) != " ":
                count += 1
            else:
                return count
        return count
