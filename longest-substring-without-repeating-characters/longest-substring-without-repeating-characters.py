class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        output = ""
        output_list = []
        
        # find all the possible substrings
        i = 0
        while (i < len(s)):
            if s[i] not in output:
                output += s[i]
        
            else:
                output_list.append(output)
                i = i - len(output) + 1
                output = s[i]
                
            if i == len(s) - 1:          # add the last substring
                output_list.append(output)
        
            i += 1
        
        #print(output_list)
        
        if (output_list):
            answer = len(output_list[0])
            for tmp in output_list:
                if len(tmp) > answer:     # find the longest substring
                    answer = len(tmp)
        else:
            answer = len(s)
        
        
        #print(len(""))   # 0
        #print(len(" "))  # 1
        
        return answer
            
            