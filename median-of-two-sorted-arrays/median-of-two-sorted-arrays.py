class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # get the sorted merged array
        merged_array = nums1
        for num in nums2:
            merged_array.append(num)
        sorted_array = sorted(merged_array)
        
        # find the median from the sorted array
        if len(sorted_array) % 2 != 0:
            return sorted_array[len(sorted_array)//2]
        else:
            return (sorted_array[len(sorted_array)//2 - 1] + sorted_array[len(sorted_array)//2]) / 2