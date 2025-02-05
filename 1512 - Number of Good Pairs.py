from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}  # Dictionary to store frequency of each number
        count = 0  # To store the number of good pairs

        # Count occurrences of each number
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Calculate the number of good pairs using the formula C(n,2) = n * (n-1) / 2
        for val in freq.values():
            count += (val * (val - 1)) // 2  # Choose 2 indices from 'val' occurrences
        
        return count
