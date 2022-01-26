class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert all uppercase letters into lowercase letters
        s = s.lower()
        # Remove all non-alphanumeric characters by using isalnum() function
        s = ''.join(c for c in s if c.isalnum())
        # Check whether it's palindrome
        return True if s == s[::-1] else False
        