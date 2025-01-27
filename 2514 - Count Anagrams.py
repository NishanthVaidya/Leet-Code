import math

class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7

        def count_word_anagrams(word):
            freq = {}
            for char in word:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            numerator = math.factorial(len(word))
            denominator = 1
            for count in freq.values():
                denominator *= math.factorial(count)
            return numerator // denominator

        words = s.split()
        result = 1
        for word in words:
            result = (result * count_word_anagrams(word)) % MOD

        return result
