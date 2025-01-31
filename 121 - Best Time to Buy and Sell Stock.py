class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1  
        maxProf = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                maxProf = max(maxProf, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return maxProf
        
