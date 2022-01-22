class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        if needle in haystack:
            index = haystack.index(needle)
        
        return index
                    
        