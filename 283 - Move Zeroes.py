class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for each in range(len(nums)):
            if nums[each] != 0:
                nums[left] , nums[each] = nums[each] , nums[left]
                left += 1
        return nums

                




        
