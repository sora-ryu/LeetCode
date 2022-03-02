class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        i = 0
        intervals.sort()
        
        while i < len(intervals)-1:
            # print(i)
            # print(intervals)
            if intervals[i+1][0] <= intervals[i][1] and intervals[i+1][1] >= intervals[i][0]:
                intervals[i][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                del intervals[i+1]
                i -= 1
            
            i += 1
        
        # final check
        if len(intervals) >= 2 and intervals[-1][0] <= intervals[-2][1] and intervals[-1][1] >= intervals[-2][0]:
            intervals[-2][0] = min(intervals[-2][0], intervals[-1][0])
            intervals[-2][1] = max(intervals[-2][1], intervals[-1][1])
            del intervals[-1]
        
        return intervals