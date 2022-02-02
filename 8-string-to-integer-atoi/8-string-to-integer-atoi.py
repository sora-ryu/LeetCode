class Solution:
    def myAtoi(self, s: str) -> int:
        
        # s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
        # find numbers by isdigit() function
        MAX_NUM = 2 ** 31 - 1
        MIN_NUM = -2 ** 31
        
        # remove the leading white spaces
        s = s.strip()
        sign = 1
        index = 0
        num = 0
        if not s:
            return num
        
        # determine sign of the number
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
        
        while index < len(s) and s[index].isdigit():
            curr_digit = ord(s[index]) - ord('0')
            if num > MAX_NUM // 10 or (num == MAX_NUM // 10 and curr_digit > 7): # here we do the check before adding current digit
                return MAX_NUM if sign == 1 else MIN_NUM
            num = num * 10 + curr_digit
            index += 1
        
        num = sign * num
        return num    