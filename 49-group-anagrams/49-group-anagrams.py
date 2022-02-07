class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # How to identify anagram?
        # => The key is to get the sorted strings and compare them.
        d = {}
        for word in strs:
            sorted_word = "".join(sorted(word))  # sorted(word) : "eat" => ['a','e','t']
            
            if not sorted_word in d.keys():
                d[sorted_word] = [word]
            else:
                d[sorted_word] += [word]
        
        return d.values()