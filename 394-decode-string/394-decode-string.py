class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:  # If we meet ']', it's time to decode string
                tmp_digit, tmp_str = '', ''
                while stack[-1] != '[':
                    tmp_str = stack.pop() + tmp_str
                stack.pop()
                print(tmp_str)
                
                while stack and stack[-1].isdigit():  # 100 => without this loop, recognize 1,0,0 / stack condition => do not pop out from the empty stack
                    tmp_digit = stack.pop() + tmp_digit
                stack.append(int(tmp_digit) * tmp_str)
                print(stack)
        
        return ''.join(stack)