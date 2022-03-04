class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        ans = []
        summation, line = 0, 0
        
        for i in range(len(s)):
            summation += widths[ord(s[i]) - 97]
            if summation > 100:
                line += 1
                summation = 0
                summation += widths[ord(s[i]) - 97]
        
        ans.append(line+1)
        ans.append(summation)
        return ans

        