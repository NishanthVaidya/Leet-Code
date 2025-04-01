class Solution:
    def compressedString(self, word: str) -> str:
        answer = ""
        left = 0
        right = 0
        count = 0

        while right < len(word):
            if word[left] == word[right] and count < 9:
                count += 1
                right += 1
            else:
                answer += str(count) + word[left]
                left = right
                count = 0
        
        # Catch the last group (loop may exit after count == 9 or at the end)
        if count > 0:
            answer += str(count) + word[left]

        return answer
