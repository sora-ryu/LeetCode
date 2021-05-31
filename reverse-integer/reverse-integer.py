class Solution(object):
    def reverse(self, x):
        to_str = str(x)
        if to_str[0] == '-':  # for negative number
            output = int(to_str[0]+ to_str[1:][::-1])
        else:                 # for positive number
            output = int(to_str[::-1])
        
        # If reversing x is out of range, then return 0.
        
        if output < -2**31 or output > 2**31 - 1:
            return 0
        else:
            return output