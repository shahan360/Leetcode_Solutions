class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We will apply Greedy as it will calculate profits for only postive slopes
        buy = 0
        total = 0
        for sell in range(1, len(prices)):
            if prices[sell] > prices[buy]:
                total += (prices[sell] - prices[buy])
            buy += 1
        return total
        