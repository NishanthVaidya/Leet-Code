class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            low, high = i + 1, n - 1

            while (low < high):
                summ = nums[i] + nums[low] + nums[high]

                if(summ == 0):
                    answer.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while(low < high):
                        if nums[low] == nums[low - 1]:
                            low += 1
                        elif nums[high] == nums[high + 1]:
                            high -= 1
                        else:
                            break
                elif(summ < 0):
                    low += 1
                elif(summ > 0):
                    high -= 1
        return answer
                
        
