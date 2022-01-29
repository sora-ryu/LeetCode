class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
        # [2,1] and [1,2]  =>  output: [1,2]
        
        nums1_count = collections.Counter(nums1)
        print(nums1_count)
        ans = []
        
        for num in nums2:
            if nums1_count[num] != 0:
                ans.append(num)
                nums1_count[num] -= 1
            print(nums1_count)
        return ans