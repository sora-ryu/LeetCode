class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #Counter: a dict subclass for counting hashable objects
        # 
        ans = []
        word2_count = {}
        
        for word2 in words2:
            tmp_count = Counter(word2)   # tmp_count: Counter({'o' : 1})
            
            for key in tmp_count:
                word2_count[key]=max(tmp_count[key], word2_count.get(key, 0))
            
        
        #print(word2_count)    # word2=["e","o"] => {'e':1, 'o':1}
        for word1 in words1:
            word1_count = Counter(word1)
            #print(word1_count)   # word1=amazon => {'a':2, 'm':1, 'z':1, 'o':1, 'n':1}
            isCheck = True
            
            for key in word2_count:
                if word1_count[key] < word2_count[key]:
                    isCheck = False
                    break
            
            if isCheck == True:
                ans.append(word1)
                
        return ans