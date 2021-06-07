class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        parentheses = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        for char in s:
            if char not in parentheses:   # open brackets
                stack.append(char)
            elif not stack or parentheses[char] != stack.pop():
                return False
        
        if len(stack) == 0:     # not ended with non-closed
            return True
                