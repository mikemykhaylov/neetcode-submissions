class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            # print(buy, sell)
            if prices[sell] < prices[buy] or prices[sell] < prices[sell - 1]:
                profit += curr
                buy = sell
                sell += 1
                curr = 0
                # print(buy, sell, profit)
                continue
            
            curr = max(curr, prices[sell] - prices[buy])
            sell += 1

        profit += curr
        return profit

        
