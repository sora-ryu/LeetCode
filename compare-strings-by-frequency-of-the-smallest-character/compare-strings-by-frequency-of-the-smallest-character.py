class Solution:
    
    '''1st attempt : time limited exceeded
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        answer = [0 for i in range(len(queries))]
        
        def f(string):    # count the frequency of the lexicographically smallest character
            smallest = sorted(string)[0]     # sorted => sort in alphabet
            count = 0
            
            for string in sorted(string):
                if string == smallest:
                    count += 1
            
            return count
            
        
        for i, query in enumerate(queries):
            for word in words:
                if f(query) < f(word):
                    answer[i] += 1
                
        return answer'''
    
    '''2nd attempt'''
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        answer = [0 for i in range(len(queries))]
        queries_freq = [0 for i in range(len(queries))]
        words_freq = [0 for i in range(len(words))]
        
        def f(string):    # count the frequency of the lexicographically smallest character
            smallest = sorted(string)[0]     # sorted => sort in alphabet
            count = 0
            
            for string in sorted(string):
                if string == smallest:
                    count += 1
            
            return count
            
        
        for i, query in enumerate(queries):
            queries_freq[i] = f(query)
            
        for j, word in enumerate(words):
            words_freq[j] = f(word)
            
        for k, num1 in enumerate(queries_freq):
            for num2 in words_freq:
                if num1 < num2:
                    answer[k] += 1
                    
        return answer