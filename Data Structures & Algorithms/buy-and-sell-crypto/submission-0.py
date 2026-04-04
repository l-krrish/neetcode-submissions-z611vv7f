class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p=0
        for i in range(len(prices)):
            curr=prices[i]
            for j in range(i,len(prices)):
                if prices[j]>prices[i]:
                    if (prices[j]-prices[i])>max_p:
                        max_p=prices[j]-prices[i]
        
        return max_p