class Solution(object):
    def isPalindrome(self, x):
        reverse = str(x)[::-1]
        if -2**31 <= x and x < 2**31:
            if reverse == str(x):
                return 1
            else:
                return 0
        else:
            return 0
        