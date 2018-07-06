# Input
# A list of stock price for some day

# Output:
# Maximum profit we can get with unlimited transactions

# Solution:
# To solve this problem, we use greedy method, 
# which means that everytime the next stock price is higher, we sell the stock out.

# Iterate over the list.
# The starting value of profit is 0.
# Everytime the current value is larger the the previous one, we add the difference to the profit.
# At the end of the iteration, we get the result.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

# Time complexity: O(n)
# Space complexity: O(1)