class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = -1
        for i in range(len(s)):
            if s.index(s[i]) == s.rindex(s[i]):
                return i
        
        return index
        