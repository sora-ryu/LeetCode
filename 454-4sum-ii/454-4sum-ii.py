class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        count = 0
        ab_sum = collections.Counter(a+b for a in nums1 for b in nums2)
        print(ab_sum)
        cd_sum = collections.Counter(c+d for c in nums3 for d in nums4)
        print(cd_sum)
        
        for i in ab_sum.keys():
            if -i in cd_sum.keys():
                count += ab_sum[i] * cd_sum[-i]
        
        return count
                    
        