class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        longest = float('inf')
        for each in (range(len(nums))):
            total += nums[each]
            while(total >= target):
                longest = min(longest, each - left + 1)
                total -= nums[left]
                left +=1
        return 0 if longest == float('inf') else longest

       
