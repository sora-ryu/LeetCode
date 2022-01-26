class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sorted(prices)[::-1]  # [7,6,5,...,1]
        
        # Time Limit Exceeded
#         max_profit = 0
#         # Set the smallest price
#         for buy in sorted(prices):
#             for i in range(prices.index(buy)+1, len(prices)):  # Find the largest price from sub-range starting from buy's index till the end.
#                 if max_profit < prices[i] - buy:
#                     max_profit = prices[i] - buy
            
#         return max_profit
        
        min_price, profit = inf, 0
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)
            # print(min_price, profit)
        
        return profit
            