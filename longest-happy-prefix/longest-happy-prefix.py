class Solution:
    def longestPrefix(self, s: str) -> str:
        happy_prefix = ""
        
        for length in range(len(s)-1):   # excluding itself
            #print(s[0:length+1])
            #print(s[len(s)-(length+1):len(s)])
            if s[0:length+1] == s[len(s)-(length+1):len(s)]:
                happy_prefix = s[0:length+1]
        
        return happy_prefix