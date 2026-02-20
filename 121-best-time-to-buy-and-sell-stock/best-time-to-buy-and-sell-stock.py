class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p=0
        min_price=float('inf')
        for price in prices:
            if min_price > price : 
                min_price=price
            if max_p < price - min_price:
                max_p = price - min_price
        return max_p
        