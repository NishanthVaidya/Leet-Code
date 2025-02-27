class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        i = 0
        
        while i < len(s):
            if i < len(s) - 1 and s[i] == 'I' and s[i + 1] == 'V':
                answer += 4
                i += 1  # Skip the next character
            elif i < len(s) - 1 and s[i] == 'I' and s[i + 1] == 'X':
                answer += 9
                i += 1
            elif i < len(s) - 1 and s[i] == 'X' and s[i + 1] == 'L':
                answer += 40
                i += 1
            elif i < len(s) - 1 and s[i] == 'X' and s[i + 1] == 'C':
                answer += 90
                i += 1
            elif i < len(s) - 1 and s[i] == 'C' and s[i + 1] == 'D':
                answer += 400
                i += 1
            elif i < len(s) - 1 and s[i] == 'C' and s[i + 1] == 'M':
                answer += 900
                i += 1
            elif s[i] == 'I':
                answer += 1
            elif s[i] == 'V':
                answer += 5
            elif s[i] == 'X':
                answer += 10
            elif s[i] == 'L':
                answer += 50
            elif s[i] == 'C':
                answer += 100
            elif s[i] == 'D':
                answer += 500
            elif s[i] == 'M':
                answer += 1000
            
            i += 1  # Move to the next character
            
        return answer
