class Solution:
    def reformatNumber(self, number: str) -> str:
        
        ans = ""
        tmp = ''.join(number.replace("-", "").split())
        print(tmp)
        
        while len(tmp) > 4:
            ans += tmp[:3] + '-'
            tmp = tmp[3:]
        
        if len(tmp) == 4:
            ans += tmp[:2] + '-' + tmp[2:]
        else:  # len(tmp) < 4
            ans += tmp
            
        return ans
    
    

        