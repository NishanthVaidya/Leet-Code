class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for each in nums:
            result ^= each
        return result



                
        
