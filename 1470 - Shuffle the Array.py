class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = n  
        res = [] 
        
        while left < n:
            res.append(nums[left])
            res.append(nums[right])
            left += 1
            right += 1
        
        return res
