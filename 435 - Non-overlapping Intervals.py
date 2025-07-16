class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        prev = intervals[0]
        output = 0

        for each in range(1, len(intervals)):
            curr = intervals[each]

            if(curr[0] < prev[1]):
                prev[1] = min(prev[1], curr[1])
                output += 1
            else:
                prev = curr
        return output
        
