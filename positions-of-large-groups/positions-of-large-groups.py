class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        ans = []
        start, i = 0, 0
        cur = s[0]
        
        while i < len(s):
            if s[i] != cur:
                if i - start > 2:
                    ans.append([start, i-1])  # It says that a group is considered large if it has 3 or more characters.
                cur = s[i]
                start = i
            i += 1
                
        if i - start > 2:                 # for the case "aaa" => [[0,2]]
            ans.append([start, i-1])
                    
        return ans