class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        total = 0
        sell = 1
        for sell in range(1,len(prices)):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                total += profit
            buy +=1
        return total