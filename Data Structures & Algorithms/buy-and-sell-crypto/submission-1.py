class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy = --> as low
        #sell = ---> as high but in the future 
        # profit is maxx

        buy = prices[0]
        profit = 0

        for price in (prices):
            if(buy < price):
                currProfit = price - buy

                profit = max(currProfit, profit)

            else:
                buy = price

        return profit

           

        
