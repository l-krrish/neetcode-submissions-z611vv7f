class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p=0
        min_price=prices[0]
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            if prices[i]-min_price>max_p:
                max_p=prices[i]-min_price
        return max_p