# Input:
# A list of stock prices, each price is for one day

# Output:
# An integer, which represents the maximum profit we can make if at most one transaction permitted.

# Solution:
# To solve this problem, we have to update the minumum price and maximum profit during the iteration of the list.
# As we have to purchase stock before sell it, we set the first price as the minimum price first.
# And the starting maximum profit is the fist price minus minimum, which is 0.

# Then, we iterate over the list. 

# we compare the current minumum price with the current price, and update the current minimum price.

# Then, we substract the current price by the current minumum price
# and compare it with the current maximum profit.

# If the caculated maximum profit is greater than the current maximum profit, then we update it.
# Or we will keep the previous maximum profit.

# At the end of iteration, we output the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        curr_min = prices[0]
        max_profit = 0
        for price in prices:
            curr_min = min(curr_min, price)
            max_profit = max(price - curr_min, max_profit)
        return max_profit

# Time complexity: O(n)
# Space complexity: O(1)