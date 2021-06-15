class Solution:
    def addBinary(self, a: str, b: str) -> str:

        c = int(a) + int(b)
        temp = []
        while c != 0:
            temp.append(c%10)
            c = c//10
        #print(temp)       # the summation will be stored in reverse order
        temp.append(0)          # prevent the case of increasing the number of digits    
        
        for i, num in enumerate(temp):       # check the usage of enumerate function!!
            #print(i, num)
            if num > 1:
                temp[i] = num % 2
                temp[i+1] += 1
        
        answer = 0
        for i, num in enumerate(temp):
            answer += num * (10**i)
            
        return str(answer)
        