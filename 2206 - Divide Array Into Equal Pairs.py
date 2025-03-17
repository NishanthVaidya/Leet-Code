class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        while i < len(nums):  
            if i + 1 >= len(nums) or nums[i] != nums[i + 1]:
                return False
            i += 2
        return True
        
