class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # [1,3],[2,6] => [1,6]
        # [1,6],[2,3] => [1,6]
        # each interval is sorted?
        # intervals are sorted? begin_i < begin_(i+1)? => No, [[1,4],[0,0]] => Let's sort first!
        # is it possible to have start_i == end_i?
        # merge if there's not space between end_i and start_(i+1)?
        
        intervals.sort()
        
        i = 0
        # for-loop starting from 0 to len(intervals)-1 index
        while i < len(intervals)-1:
            # consider only two intervals (ith and (i+1)th)
            # if end_i < start_(i+1): it means that there's a space between two intervals
            if intervals[i][1] < intervals[i+1][0]:
                # do not merge
                i += 1
                continue
            # else: merge
            else:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals[i][0] = min(intervals[i][0], intervals[i+1][0])
                del intervals[i+1]
        
        return intervals
                
        