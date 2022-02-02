class Solution:
    def maxArea(self, height: List[int]) -> int:
        # More Faster Version : O(n)
        # Starting with the farthest two lines (biggest horizontal value), find the high vertical lines such that largest area. In this way, we don't have to do brute force search.
    
        left, right = 0, len(height)-1
        max_area = 0
        
        while left != right:
            
            # Keep the taller line
            if height[left] < height[right]:
                current_area = height[left] * (right-left)
                left += 1
            
            else:
                current_area = height[right] * (right-left)
                right -= 1

            max_area = max(max_area, current_area)

        return max_area
        
        
#         # Time Limited Exceeded : O(n^2)
#         if len(height) == 2:
#             return min(height[0],height[1]) * 1
#         max_area = 0
#         for h1_index in range(len(height)):
#             for h2_index in range(h1_index+1, len(height)):
#                 current_area = min(height[h1_index], height[h2_index]) * abs(h1_index - h2_index) 
#                 if current_area > max_area:
#                     max_area = current_area
        
#         return max_area

        