"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""
Brute force:
class Solution(object):
   def maxProfit(self,prices)

    n= len(prices)
    max profit == 0

   for i in range(n):
      for j in range(i+1,n)# we did i+1 because we can't buy and sell stocks in the same day itself in stock market.
      profit= prices[j]- prices[i]
       if profit > max_profit:
                    max_profit = profit
            
        return max_profit
Dry run:
Buy day 0, sell day 1: profit = -6 (not > 0, so max_profit stays 0)
Buy day 0, sell day 2: profit = -2(5-7) (not > 0, so max_profit stays 0)
Buy day 1, sell day 2: profit = 4 (4 > 0, so max_profit = 4)
Buy day 1, sell day 4: profit = 5 (5 > 4, so max_profit = 5) ✅
Continue checking...

example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.



 
