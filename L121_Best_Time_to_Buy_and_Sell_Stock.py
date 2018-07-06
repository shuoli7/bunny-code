# Input:
# A list of stock price on one day

# Output:
# The maximum profit we can get if at most one transaction permitted.

# Solution:
# Two solve this problem, we have to update the minumum price and maximum profit during the iteration of the list.
# As we have to purchase stock before sell it, we set the first value as the minimum price first.
# And the starting maximum profit is the fist value minus minimum, which is 0.

# Then, we iterate over the list. 

# If the current price is less than the minumum, we update the minimum.

# If the current price is larger than the minumum, we substract the current price by the minumum
# and compare it with the current maximum.

# If the caculated maximum is greater than the maximum, then we update it.
# Or we will keep the previous maximum.

# At the end of iteration, we output the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Edge case: if the input list is empty or all to be zero, the result is 0.
        if not prices:
            return 0
        
        minimum = prices[0]
        maximum = 0
        for price in prices:
            minimum = min(minimum, price)
            maximum = max(price - minimum, maximum)
        return maximum

# Time complexity: O(n)
# Space complexity: O(1)