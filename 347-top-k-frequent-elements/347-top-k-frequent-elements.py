class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        x = Counter(nums)
        
        return [x.most_common(k)[i][0] for i in range(len(x.most_common(k)))]
        