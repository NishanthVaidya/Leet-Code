class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        richKid = max(candies)
        answer = []
        for each in range(len(candies)):
            if candies[each] + extraCandies >= richKid:
                answer.append(True)
            else:
                answer.append(False)
        return answer

        
