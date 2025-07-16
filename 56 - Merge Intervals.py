class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        output = []
        prev = intervals[0]

        for each in range(1, len(intervals)):
            curr = intervals[each]
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1]) 
            else:
                output.append(prev)
                prev = curr
        output.append(prev)
        return output
        
