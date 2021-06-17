class Solution:
    ''' 1st attempt: time limited error (TLE)'''
#     def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
#         result = 0
#         result_list = []
        
#         def compare(remember: List[int], pair_copy: List[int]) -> int:
#             for element in remember:
#                 #print(element, remember, pair_copy)
#                 val = element in pair_copy
#                 if val:
#                     pair_copy.remove(element)
                
                
#             return 1 if not pair_copy else 0      # if not pair = if pair is empty
            
#         for i in range(len(dominoes)):
#             remember = dominoes[i]
#             for j, pair in enumerate(dominoes):
#                 if i >= j:        # try to avoid duplicated comparison
#                     continue
#                 #print(i,j)
#                 pair_copy = pair[:]          # deep copy(doesn't affect changing) vs shallow copy(affect changing)
#                 result += compare(remember, pair_copy)
#                 # if compare(remember, pair_copy) != 0:
#                 #     print(i,j, result, remember, pair)
                
#             result_list.append(result)
#             result = 0
        
        
#         print(result_list)
        
#         return sum(result_list)     # sum function: returns the summation of every list element
    ''' 2nd attempt: Use hashtable by using dictionary'''
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = {}
        
        for pair in dominoes:
            key = min(pair) + 10 * max(pair)    # important process of making unique and fair key.
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1
                
        # In order to avoid duplicated counting, use combination.
        # Thus, 1 won't be counted.
        return sum(c*(c-1)//2 for c in counts.values())
        
            