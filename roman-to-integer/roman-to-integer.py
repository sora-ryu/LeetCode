class Solution(object):
        
    def romanToInt(self, s):
        output = 0
        roman_dic = {"I":1, "V":5, "X": 10, "L": 50, "C": 100, "D":500, "M":1000}
        
        for i in range(len(s)-1):
            if roman_dic[s[i]] < roman_dic[s[i+1]]:      # for subtraction
                output -= roman_dic[s[i]]
            else:
                output += roman_dic[s[i]]
                
        output += roman_dic[s[len(s)-1]]    # for the last element
        
        return output
    