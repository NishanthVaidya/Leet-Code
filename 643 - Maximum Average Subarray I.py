class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        currentSum = 0
        average = 0
        for i in range(k):
            currentSum += nums[i]

        average = currentSum/k
        maxAv = average
        for i in range(k,len(nums)):
            currentSum += nums[i]
            currentSum -= nums[i-k]

            average = currentSum/k
            maxAv = max(maxAv, average)
        return maxAv




        
