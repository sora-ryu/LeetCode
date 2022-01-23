class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Increment the integer first
        digits[len(digits)-1] += 1
        
        # Traverse the list "digits" in a reversed order
        # for i in reversed(digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] > 9 and i != 0:   # Except for the most significant order
                digits[i] = 0
                digits[i-1] += 1
            elif digits[i] > 9 and i == 0:   # Special case (the most siginifcant order)
                digits[i] = 0
                digits.insert(0, 1)  # increase the size of digits
        
        return digits
                
        