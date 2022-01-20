class Solution:
    def minimumDeletions(self, s: str) -> int:
        # the order should be 'a' and then 'b'
        a, b = s.count('a'), 0
        res = a + b
        for char in s:
            if char == 'a':
                a -= 1
            else:
                b += 1
            res = min(res, a + b)

        return res