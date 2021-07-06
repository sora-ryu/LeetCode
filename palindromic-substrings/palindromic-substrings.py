class Solution:
    def countSubstrings(self, s: str) -> int:
        count = [1 for i in range(len(s))]   # [1, 1, 1, ..., 1]
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:       # my_str[::-1] : reverse my_str
                    count[i] += 1
        
        
        return sum(count)