class Solution:
    def largestOddNumber(self, num: str) -> str:
        '''
        num[:0] => nothing, empty list
        num[0:] => whole list
        
        largest_odd = "12345"
        print(largest_odd[0:])    # 12345
        print(largest_odd[:0])    # nothing
        print(largest_odd[:4])    # 1234
        print(largest_odd[:5])    # 12345
        '''
        
        largest_odd = ""
        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                largest_odd = num[:i+1]
        
        return largest_odd