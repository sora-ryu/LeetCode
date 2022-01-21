class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # The longest palindromic substring would be 's' itself if it's consisted of one character
        if s == len(s) * s[0]:
            return s
        
        # For the other cases:
        # Starting from the middle index, try to add character if both sides (left and right) are same or they are consisted of one character
        
        max_len = 1
        answer = ""
        
        def find(left, right, cur_len):
            nonlocal max_len, answer
            
            while 0<=left and right<len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
                cur_len += 2
            if cur_len > max_len:
                max_len = cur_len
                answer = s[left+1:right]
                print(max_len, answer, left, right)
            
            
            
        for i in range(1, len(s)):
            find(i, i, 1)  # for odd
            find(i-1, i, 2) # for even
        
        return answer