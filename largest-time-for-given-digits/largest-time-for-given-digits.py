from collections import Counter

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        largest_time = ""
        
        arr.sort(reverse=True)   # sort the array in descending order
        
        for n1, n2, n3, n4 in itertools.permutations(arr):  # use permutation!
            hour, minute = n1*10+n2, n3*10+n4
            #print(hour, minute)
            
            if 0<=hour<24 and 0<=minute<60:
                largest_time = str(n1)+str(n2)+":"+str(n3)+str(n4)   # in order to pass this case: [0,0,0,0] => "00:00"
                break
                
        return largest_time