from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        
        count = 0
        left = 0
        while left < n - 2:
            if nums[left] == 0:
                nums[left] ^= 1
                nums[left + 1] ^= 1
                nums[left + 2] ^= 1
                count += 1

            left += 1

        if any(num == 0 for num in nums):
            return -1
        
        return count
