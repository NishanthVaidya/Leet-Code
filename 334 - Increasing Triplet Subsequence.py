class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for each in nums:
            if each <= first:
                first = each
            elif each <= second:
                second = each
            else:
                return True
        return False
