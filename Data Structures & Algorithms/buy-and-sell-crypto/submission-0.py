class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprofit=0
        for price in prices[1:]:
            if price<minprice:
                minprice=price
            maxprofit=max(maxprofit,price-minprice)
        return maxprofit