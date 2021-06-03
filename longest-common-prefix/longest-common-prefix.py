class Solution(object):
    def longestCommonPrefix(self, strs):
        
        # find the shortest length word
        minimal_word = strs[0]
        for words in strs:
            if words == "":
                return ""
            if len(words) < len(minimal_word):
                minimal_word = words
        
        else:
            common_prefix = ""
            breaker = False    # boolean flag that helps to break out nested for loop
            for i in range(len(minimal_word)):
                temp = strs[strs.index(minimal_word)][i]
                for j in range(len(strs)):
                    if (strs[j][i] != temp):
                        breaker = True
                        break
                if breaker == True:
                    break
                common_prefix += temp
            
        return common_prefix
    