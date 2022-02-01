class Solution:
    def countAndSay(self, n: int) -> str:
        #
        "1"
        "11"
        "21"
        "1211"
        "111221"
        "312211"
        "13112221"
        "1113213211"
        #

#         def directed_count_value(s):
#             temp, count = '', 1
#             for i in range(len(s) - 1):
#                 if s[i] == s[i + 1]:
#                     count += 1
#                 else:
#                     temp += str(count) + s[i]
#                     count = 1

#             temp += str(count) + s[-1]
#             return temp

#         result = '1'
#         for _ in range(n - 1):
#             result = directed_count_value(result)

#         return result
    
        if n == 1:
            return "1"
        
        base = "1"
        def recursion(base: str) -> str:
            
            string, count = "", 1
            for i in range(len(base)-1):
                if base[i] == base[i+1]:
                    count += 1
                else:
                    string += "".join(str(count) + base[i])
                    count = 1
                    
            string += "".join(str(count) + base[-1])     
            return string
            
            
        for _ in range(n-1):
            base = recursion(base)
            
        return base
