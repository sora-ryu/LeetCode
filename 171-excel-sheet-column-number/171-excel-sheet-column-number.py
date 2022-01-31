class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        # Python ord() function returns the Unicode code from a given character.
        # ord('A') = 65
        # ord('B') = 66
        # ord('Z') = 90
        
        column_num = 0
        for order in range(len(columnTitle)-1, -1, -1):
            unicode = ord(columnTitle[order])
            print(unicode)
            column_num += (unicode - 64) * (26 ** (len(columnTitle)-1-order))
            print(column_num)
        return column_num